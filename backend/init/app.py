import logging
import traceback

from flasgger import Swagger
from flask import Flask, g, request, Response, jsonify
from werkzeug.exceptions import NotFound, InternalServerError, ServiceUnavailable, BadRequest, Forbidden, \
    MethodNotAllowed, HTTPException

from init.logger import init_logger
from init.swagger import template
from route.url import register_router
from setting.config import config
from util.error import ThirdPartyServiceErr, ParameterErr


def init_app() -> Flask:
    """init flask app"""
    app = Flask(__name__)
    app.config.from_object(config)

    register_router(app)
    init_before_req_hook(app)
    init_after_req_hook(app)

    level = app.config.get('LOG_LEVEL')
    mode = app.config.get('LOG_MODE')
    path = app.config.get('LOG_FILE_PATH')
    init_logger(level=level, mode=mode, path=path)

    # Enable the documentation api only in debug mode
    if app.config.get('DEBUG'):
        swagger = Swagger(app=app, template=template)

    return app


def init_before_req_hook(app: Flask) -> None:
    @app.before_request
    def record_request() -> None:
        """record request data in debug mode"""
        g.logger = logging.getLogger('logger')
        g.logger.debug('[request_log] {ip} {method} {url}'.format(
            ip=request.remote_addr,
            method=request.method,
            url=request.url
        ))


def init_after_req_hook(app: Flask) -> None:
    @app.errorhandler(Exception)
    def handle_error(e) -> Response:
        """handle exceptions globally and return friendly message"""
        if isinstance(e, ThirdPartyServiceErr):
            g.logger.error(traceback.format_exc())
            # message = 'Service temporarily unavailable, please contact the system administrator, error code: {}'.format(e.code)
            message = e.description
            status_code = ServiceUnavailable.code
        elif isinstance(e, ParameterErr):
            message = e.description
            status_code = BadRequest.code
        elif isinstance(e, BadRequest):
            # message = 'friendly message for 400'
            message = e.description
            status_code = BadRequest.code
        elif isinstance(e, Forbidden):
            message = 'friendly message for 403'
            status_code = Forbidden.code
        elif isinstance(e, NotFound):
            message = 'friendly message for 404'
            status_code = NotFound.code
        elif isinstance(e, MethodNotAllowed):
            message = 'friendly message for 405'
            status_code = MethodNotAllowed.code
        elif isinstance(e, InternalServerError):
            message = 'friendly message for 500'
            status_code = InternalServerError.code
        elif isinstance(e, HTTPException) and 500 < e.code < 600:
            message = 'Service unavailable, please contact the system administrator'
            status_code = e.code
        else:
            g.logger.error(traceback.format_exc())
            message = 'Unknown error'
            status_code = InternalServerError.code
        response = jsonify(dict(message=message))
        response.status_code = status_code
        return response

    @app.after_request
    def record_response(response: Response) -> Response:
        """record response data in debug mode"""
        g.logger.debug('[response_log] {ip} {method} {url}'.format(
            ip=request.remote_addr,
            method=request.method,
            url=request.url,
            data=response.json
        ))

        # Allow cross-domain access only in debug mode
        # response.headers['Access-Control-Allow-Origin'] = '*'

        return response
