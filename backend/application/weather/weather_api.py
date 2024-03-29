import traceback

from flasgger import swag_from
from flask import jsonify, request, current_app, Response

from service.openweathermap import get_weather_overview, get_weather_details
from util.code import MAP_BOX_SERVICE_RESPONSE_ERR, PARAMETER_TYPE_ERR, OPEN_WEATHER_MAP_SERVICE_ERR, \
    OPEN_WEATHER_MAP_SERVICE_RESPONSE_ERR, PARAMETER_VALUE_ERR
from util.error import ThirdPartyServiceErr, ParameterErr


@swag_from('/doc/swagger/weather/overview.yml')
def get_weather_overview_view() -> Response:
    """get weather overview by longitude and latitude"""

    # check data type
    try:
        longitude = float(request.args.get('longitude'))
        latitude = float(request.args.get('latitude'))
    except Exception:
        raise ParameterErr(code=PARAMETER_TYPE_ERR, description='Longitude and latitude should be integer or float')

    # check data value
    if (longitude < -180 or longitude > 180) or (latitude < -90 or latitude > 90):
        raise ParameterErr(
            code=PARAMETER_VALUE_ERR,
            description='Longitude should be between -180 and 180, latitude should be between -90 and 90,'
        )

    try:
        weather_info = get_weather_overview(
            longitude=longitude,
            latitude=latitude,
            app_id=current_app.config.get('OPEN_WEATHER_MAP_APP_ID')
        )
    except Exception:
        raise ThirdPartyServiceErr(code=OPEN_WEATHER_MAP_SERVICE_ERR, description=traceback.format_exc())

    # check response data
    if weather_info.get('cod') != 200:
        raise ThirdPartyServiceErr(
            code=MAP_BOX_SERVICE_RESPONSE_ERR,
            description='response data: {}'.format(weather_info)
        )
    return jsonify(weather_info)


@swag_from('/doc/swagger/weather/details.yml')
def get_weather_details_view() -> Response:
    """get weather details by longitude and latitude"""

    # check data type
    try:
        longitude = float(request.args.get('longitude'))
        latitude = float(request.args.get('latitude'))
    except Exception:
        raise ParameterErr(code=PARAMETER_TYPE_ERR, description='Longitude and latitude should be integer or float')

    # check data value
    if not -180 <= longitude <= 180 or not -90 <= latitude <= 90:
        raise ParameterErr(
            code=PARAMETER_VALUE_ERR,
            description='Longitude should be between -180 and 180, latitude should be between -90 and 90, now'
        )

    try:
        weather_info = get_weather_details(
            longitude=longitude,
            latitude=latitude,
            app_id=current_app.config.get('OPEN_WEATHER_MAP_APP_ID')
        )
    except Exception:
        raise ThirdPartyServiceErr(code=OPEN_WEATHER_MAP_SERVICE_ERR, description=traceback.format_exc())

    # check response data
    if weather_info.get('cod') and weather_info.get('cod') != 200:
        raise ThirdPartyServiceErr(
            code=OPEN_WEATHER_MAP_SERVICE_RESPONSE_ERR,
            description='response data: {}'.format(weather_info)
        )

    return jsonify(weather_info)
