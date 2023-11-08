"""
Class for the addy.io python bindings
"""

import requests
import configparser

class AddyApiDetails:
    URL = "https://app.addy.io/api/v1/"

    def __init__(self) -> None:
        """Read key from .cfg file throw error if it can't be found."""
        self.api_key = ""
        try:
            with open("addy_key.cfg", "r") as f:
                self.api_key = f.readline()
        except:
            if not self.api_key:
                raise('No api key present: Run load-key')
    
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
        
    def get_api_token_details(self) -> dict[str]:
        """Return details about the supplied api key.


        Returns:
          If the key is valid, json with three keys will be returned  
          {'name': 'Batman', 'created_at': '1939-05-28 01:27:00', 'expires_at': '2024-12-12 01:11:11'}
  
          If the key is invalid you'll get an unauth error
        """

        response = requests.request('GET', AddyApiDetails.URL+'api-token-details', 
                                    headers=self._get_headers())
        
        return response.json()
        
    def get_account_details(self) -> dict:
        """Return all account details associated with the api key.
        
        Returns:
            json of associated account details
        """

        response = requests.request('GET', AddyApiDetails.URL+'account-details', 
                                    headers=self._get_headers())
    
        return response.json()