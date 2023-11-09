"""
Class for the addy.io python bindings
"""

import requests
import json

from pyaddy.API.url import AddyURL
from pyaddy.API.addy_key import AddyKey

class AddyApiDetails:

    def __init__(self) -> None:
        """Read key from .cfg file throw error if it can't be found."""
        self.url = AddyURL()
        self.api_key = AddyKey().load_key()

    
    def _get_headers(self) -> dict:
        """Return headers used for request.
        
        Return:
            Dict[str]
        """
        headers = {
        'Authorization': f'Bearer {self.api_key}',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
        }

        return headers
        
    def get_api_details(self) -> dict[str]:
        """Return details about the supplied api key.


        Returns:
          If the key is valid, json with three keys will be returned  
          {'name': 'Batman', 'created_at': '1939-05-28 01:27:00', 
          'expires_at': '2024-12-12 01:11:11'}
  
          If the key is invalid you'll get an unauth error
        """

        response = requests.request('GET', self.url.api_details(), 
                                    headers=self._get_headers())
        
        return json.dumps(response.json(), indent=4)
        
    def get_account_details(self) -> dict:
        """Return all account details associated with the api key.
        
        Returns:
            json of associated account details
        """

        response = requests.request('GET', self.url.account_details(), 
                                    headers=self._get_headers())
    
        return json.dumps(response.json(), indent=4)