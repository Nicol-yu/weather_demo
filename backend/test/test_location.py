import random
import string
import time


class TestLocation(object):

    request_path = 'api/location/city'

    def test_location_available(self, client):
        response = client.get(self.request_path, query_string=dict(city_name='beijing'))
        locations_info = response.json
        features = locations_info.get('features')
        assert response.status_code == 200
        assert features is not None
        assert isinstance(features, list)

    def test_location_succeed(self, client):
        # test random value
        for i in range(3):
            time.sleep(1)
            city_name = ''.join(random.choices(string.ascii_letters, k=random.randint(0, 32)))
            response = client.get(self.request_path, query_string=dict(city_name=city_name))
            locations_info = response.json
            features = locations_info.get('features')
            assert response.status_code == 200
            assert features is not None
            assert isinstance(features, list)
        # test boundary value
        # test min len
        response = client.get(self.request_path, query_string=dict(city_name=''))
        locations_info = response.json
        features = locations_info.get('features')
        assert response.status_code == 200
        assert features is not None
        assert isinstance(features, list)
        # test max len
        city_name = ''.join(random.choices(string.ascii_letters, k=32))
        response = client.get(self.request_path, query_string=dict(city_name=city_name))
        locations_info = response.json
        features = locations_info.get('features')
        assert response.status_code == 200
        assert features is not None
        assert isinstance(features, list)

    def test_location_city_name_exceed_limit_len(self, client):
        city_name = ''.join(random.choices(string.ascii_letters, k=33))
        response = client.get(self.request_path, query_string=dict(city_name=city_name))
        assert response.status_code == 400

