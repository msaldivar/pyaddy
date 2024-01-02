"""
Class for the domain actions
"""

import requests
from pyaddy.API.addy_key import AddyKey
from pyaddy.API.url import AddyURL

class Domain:
    def __init__(self) -> None:
        self.url = AddyURL()
        self.api_key = AddyKey().load_key()

    def get_all_domain_options(self) -> dict:
        """Retrieve all domain options"""

        response = requests.request(
            "GET", self.url.get_all_domain_options(), headers=self.url.get_headers(self.api_key)
        )
        return response