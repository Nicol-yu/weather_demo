from flask import Blueprint, Flask

from application.weather import weather_api
from application.location import location_api


class MyBlueprint(Blueprint):

    def register_url(self, rule, f, **options) -> None:
        endpoint = options.pop('endpoint', f.__name__)
        self.add_url_rule(rule, endpoint, f, **options)


def register_router(app: Flask) -> None:
    pre_addr = '/api'

    location_blue = MyBlueprint('location_blue', 'application.location.location_api', url_prefix=pre_addr)
    location_blue.register_url(rule='/location/city', f=location_api.get_cities_and_locations_view, methods=['GET'])

    weather_blue = MyBlueprint('weather_blue', 'application.weather.weather_api', url_prefix=pre_addr)
    weather_blue.register_url(rule='/weather/overview', f=weather_api.get_weather_overview_view, methods=['GET'])
    weather_blue.register_url(rule='/weather/details', f=weather_api.get_weather_details_view, methods=['GET'])

    app.register_blueprint(location_blue)
    app.register_blueprint(weather_blue)
