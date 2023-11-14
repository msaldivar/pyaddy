import unittest
from pyaddy.API.api_details import AddyApiDetails


class TestApiDetailsCmds(unittest.TestCase):

    def setUp(self) -> None:
        self.addy_api_details = AddyApiDetails()

    def test_check_api_key_details(self):
        """Test getting api key details"""
        resp = self.addy_api_details.get_api_details()
        details = resp.json()

        assert resp.status_code == 200, f'Getting API details did not return 200: {resp.status_code}'
        assert len(details) == 3, f'Api details should have 3 keys: {len(details)} keys were found'
        assert ['name', 'created_at', 'expires_at'] == list(details.keys()), f'Missing key in resp: {details}'

    def test_get_account_details(self):
        """Test getting addy account details"""
        resp = self.addy_api_details.get_account_details()
        
        assert resp.status_code == 200, f'Getting account details did not return 200: {resp.status_code}'
