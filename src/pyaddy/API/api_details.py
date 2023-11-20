"""
Class for the api and account details
"""

import requests
from pyaddy.API.addy_key import AddyKey
from pyaddy.API.url import AddyURL


class AddyApiDetails:
    def __init__(self) -> None:
        """Read key from .cfg file throw error if it can't be found."""
        self.url = AddyURL()
        self.api_key = AddyKey().load_key()

    def get_api_details(self) -> dict[str]:
        """Return details about the supplied api key.


        Returns:
          If the key is valid, json with three keys will be returned
          {'name': 'Batman', 'created_at': '1939-05-28 01:27:00',
          'expires_at': '2024-12-12 01:11:11'}

          If the key is invalid you'll get an unauth error
        """

        response = requests.request(
            "GET", self.url.api_details(), headers=self.url.get_headers(self.api_key)
        )
        return response

    def get_account_details(self) -> dict:
        """Return all account details associated with the api key.

        Returns:
            json of associated account details
        """

        response = requests.request(
            "GET",
            self.url.account_details(),
            headers=self.url.get_headers(self.api_key),
        )

        return response
