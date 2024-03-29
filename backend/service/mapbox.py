from typing import Dict, Any

import requests


def search_city(city_name: str, token: str) -> Dict[str, Any]:
    params = {
        'types': 'place',
        'access_token': token,
    }

    response = requests.request(
        method='GET',
        url='https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json'.format(city_name),
        params=params
    )
    cities_info = response.json()
    return cities_info
