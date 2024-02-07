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
    
    def get_all_domains(self) -> dict:
        """Retrieves all domains"""
        
        response = requests.request(
            "GET", self.url.get_all_domains(), headers=self.url.get_headers(self.api_key)
        )
        return response

    def get_specific_domain(self, id) -> dict:
        """Get a specific domain"""

        response = requests.request(
            "GET", self.url.get_specific_domain(id), headers=self.url.get_headers(self.api_key)
        )
        return response
    
    def create_new_domain(self, params: dict) -> dict:
        """Create a new domain"""

        response = requests.request(
            "POST", 
            self.url.create_new_domain(), 
            headers=self.url.get_headers(self.api_key),
            params=params
        )

        if response.status_code != 201:
            raise(f"Domain {params['domain']} failed to be created")