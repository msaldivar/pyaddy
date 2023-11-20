"""
Class for alias actions
"""

import requests
from pyaddy.API.addy_key import AddyKey
from pyaddy.API.url import AddyURL


class Aliases:
    def __init__(self) -> None:
        self.url = AddyURL()
        self.api_key = AddyKey().load_key()

    def get_all_aliases(self, params: dict) -> dict:
        """Get all ACTIVE aliases SORTED by CREATED_AT"""

        response = requests.request(
            "GET",
            self.url.get_all_aliases(),
            headers=self.url.get_headers(self.api_key),
            params=params,
        )

        return response

    def get_specific_alias(self, id: str) -> dict:
        """Get a specific alias"""

        response = requests.request(
            "GET",
            self.url.get_specific_alias().format(id),
            headers=self.url.get_headers(self.api_key),
        )

        return response

    def create_new_alias(self, payload: dict) -> dict:
        """Creats a new alias"""

        response = requests.request(
            "POST",
            self.url.create_new_alias(),
            headers=self.url.get_headers(self.api_key),
            json=payload,
        )
        return response

    def update_specific_alias(self, id: str, payload: dict) -> dict:
        """Update a specific alias"""

        response = requests.request(
            "PATCH",
            self.url.get_specific_alias().format(id),
            headers=self.url.get_headers(self.api_key),
            json=payload,
        )

        return response

    def restore_specific_alias(self, id: str) -> dict:
        """Restores a specific deleted alias"""

        response = requests.request(
            "PATCH",
            self.url.restore_specific_alias().format(id),
            headers=self.url.get_headers(self.api_key),
        )
        return response

    def delete_specific_alias(self, id: str) -> dict:
        """Delete a specific alias"""

        response = requests.request(
            "DELETE",
            self.url.delete_alias().format(id),
            headers=self.url.get_headers(self.api_key),
        )

        if response.status_code != 204:
            raise (f"Alias {id} not deleted")
        return response

    def forget_specific_alias(self, id: str) -> dict:
        """Forget a specific alias"""

        response = requests.request(
            "DELETE",
            self.url.forget_alias().format(id),
            headers=self.url.get_headers(self.api_key),
        )
        if response.status_code != 204:
            raise (f"Alias {id} not forgotten")
        return response

    def activate_alias(self, payload: dict) -> dict:
        """Activate an alias"""

        response = requests.request(
            "POST",
            self.url.activate_alias(),
            headers=self.url.get_headers(self.api_key),
            json=payload,
        )
        return response

    def deactivate_alias(self, id: str) -> dict:
        """Deactivate alias"""

        response = requests.request(
            "DELETE",
            self.url.deactivate_alias().format(id),
            headers=self.url.get_headers(self.api_key),
        )
        if response.status_code != 204:
            raise (f"Alias {id} not deactivated")
        return response
