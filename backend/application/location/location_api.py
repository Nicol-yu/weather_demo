import traceback

from flasgger import swag_from
from flask import jsonify, request, current_app, Response

from service.mapbox import search_city
from util.code import PARAMETER_LENGTH_ERR, MAP_BOX_SERVICE_ERR
from util.error import ParameterErr, ThirdPartyServiceErr


@swag_from('/doc/swagger/location/city.yml')
def get_cities_and_locations_view() -> Response:
    """search city coordinates by name"""
    city_name = request.args.get('city_name')

    if len(city_name) < 0 or len(city_name) > 32:
        raise ParameterErr(
            code=PARAMETER_LENGTH_ERR,
            description='The length of the city_name should be between 0 and 32'
        )

    try:
        cities_info = search_city(city_name=city_name, token=current_app.config.get('MAP_BOX_TOKEN'))
    except Exception:
        raise ThirdPartyServiceErr(code=MAP_BOX_SERVICE_ERR, description=traceback.format_exc())

    return jsonify(cities_info)
