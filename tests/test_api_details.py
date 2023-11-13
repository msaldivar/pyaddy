import unittest
from pyaddy.API.api_details import AddyApiDetails



class TestApiDetailsCmds(unittest.TestCase):

    def setUp(self) -> None:
        """"""

    def test_check_api_key_details(self):
        resp = AddyApiDetails().get_api_details()
        details = resp.json()

        assert resp.status_code == 200, 'Api didnt return 200'
        assert len(details) == 3, 'Api details should have 3 keys'
        assert ['name', 'created_at', 'expires_at'] == list(details.keys()), f'Missing key in resp: {details}'

    def test_get_account_details(self):
        resp = AddyApiDetails().get_account_details()
        details = resp.json()
        breakpoint()
        assert resp.status_code == 200, 'Api didnt return 200'

        