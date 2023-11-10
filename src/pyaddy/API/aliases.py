"""
Class for alias actions
"""

import requests

from pyaddy.API.url import AddyURL
from pyaddy.API.addy_key import AddyKey

class Aliases:

    def __init__(self) -> None:
        self.url = AddyURL()
        self.api_key = AddyKey().load_key()

    def _build_params(self) -> dict:

        params = {
        # 'filter[deleted]': 'with',
        'filter[active]': 'true',
        # 'filter[search]': 'johndoe',
        'sort': '-created_at',
        # 'page[number]': '1',
        # 'page[size]': '10',
        # 'with': 'recipients',
        }

    def get_all_aliases(self) -> dict:
        """"""

        response = requests.request('GET', self.url.get_all_aliases(),
                                    headers=self.url.get_headers(self.api_key), params=self._build_params())
        
        return response.json()