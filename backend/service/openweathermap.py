from typing import Dict, Any

import requests


def get_weather_overview(longitude: float, latitude: float, app_id: str) -> Dict[str, Any]:
    params = {
        'appid': app_id,
        'units': 'imperial',
        'lat': latitude,
        'lon': longitude
    }

    response = requests.request(
        method='GET',
        url='https://api.openweathermap.org/data/2.5/weather',
        params=params
    )
    weather_info = response.json()
    return weather_info


def get_weather_details(longitude: float, latitude: float, app_id: str) -> Dict[str, Any]:
    params = {
        'appid': app_id,
        'units': 'imperial',
        'lat': latitude,
        'lon': longitude,
        'exclude': '{part}'
    }

    response = requests.request(
        method='GET',
        url='https://api.openweathermap.org/data/2.5/onecall',
        params=params
    )
    weather_info = response.json()
    return weather_info
