import random
import time


class TestWeatherOverview(object):

    request_path = 'api/weather/overview'

    def test_weather_overview_available(self, client):
        param = dict(
            latitude=23.130196,
            longitude=113.259294
        )
        response = client.get(self.request_path, query_string=param)
        weather_info = response.json
        assert response.status_code == 200
        assert weather_info.get('cod') == 200

    def test_weather_overview_succeed(self, client):
        # test random value
        for i in range(3):
            time.sleep(1)
            longitude = random.randint(-180, 180) + random.randint(0, 99) / 100
            latitude = random.randint(-90, 90) + random.randint(0, 99) / 100
            response = client.get(self.request_path, query_string=dict(latitude=latitude, longitude=longitude))
            weather_info = response.json
            assert response.status_code == 200
            assert weather_info.get('cod') == 200
        # test boundary value
        # test min value
        response = client.get(self.request_path, query_string=dict(latitude=-90, longitude=-180))
        weather_info = response.json
        assert response.status_code == 200
        assert weather_info.get('cod') == 200

        # test max value
        response = client.get(self.request_path, query_string=dict(latitude=90, longitude=180))
        weather_info = response.json
        assert response.status_code == 200
        assert weather_info.get('cod') == 200

    def test_weather_overview_wrong_type_longitude(self, client):
        param = dict(
            latitude=23.130196,
            longitude='aaaa'
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400

    def test_weather_overview_wrong_type_latitude(self, client):
        param = dict(
            latitude='bbb',
            longitude=113.259294
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400

    def test_weather_overview_wrong_value_latitude(self, client):
        param = dict(
            latitude=-91,
            longitude=113.259294
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400

    def test_weather_overview_wrong_value_longitude(self, client):
        param = dict(
            latitude=23.130196,
            longitude=181
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400


class TestWeatherDetails(object):

    request_path = 'api/weather/details'

    def test_weather_details_available(self, client):
        param = dict(
            latitude=23.130196,
            longitude=113.259294
        )
        response = client.get(self.request_path, query_string=param)
        weather_info = response.json
        assert response.status_code == 200
        assert weather_info.get('cod') is None
        assert weather_info.get('lat') is not None and weather_info.get('lon') is not None

    def test_weather_details_succeed(self, client):
        for i in range(3):
            time.sleep(1)
            longitude = random.randint(-180, 180) + random.randint(0, 99) / 100
            latitude = random.randint(-90, 90) + random.randint(0, 99) / 100
            response = client.get(self.request_path, query_string=dict(latitude=latitude, longitude=longitude))
            weather_info = response.json
            assert response.status_code == 200
            assert weather_info.get('cod') is None
            assert weather_info.get('lat') is not None and weather_info.get('lon') is not None

        # test boundary value
        # test min value
        response = client.get(self.request_path, query_string=dict(latitude=-90, longitude=-180))
        weather_info = response.json
        assert response.status_code == 200
        assert weather_info.get('cod') is None
        assert weather_info.get('lat') is not None and weather_info.get('lon') is not None

        # test max value
        response = client.get(self.request_path, query_string=dict(latitude=90, longitude=180))
        weather_info = response.json
        assert response.status_code == 200
        assert weather_info.get('cod') is None
        assert weather_info.get('lat') is not None and weather_info.get('lon') is not None

    def test_weather_details_wrong_type_longitude(self, client):
        param = dict(
            latitude=23.130196,
            longitude='aaaa'
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400

    def test_weather_details_wrong_type_latitude(self, client):
        param = dict(
            latitude='bbb',
            longitude=113.259294
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400

    def test_weather_details_wrong_value_latitude(self, client):
        param = dict(
            latitude=-91,
            longitude=113.259294
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400

    def test_weather_details_wrong_value_longitude(self, client):
        param = dict(
            latitude=23.130196,
            longitude=181
        )
        response = client.get(self.request_path, query_string=param)
        assert response.status_code == 400
