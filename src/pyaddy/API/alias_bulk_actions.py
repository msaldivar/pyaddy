"""
Class for all alias bulk actions
"""


import requests
from pyaddy.API.addy_key import AddyKey
from pyaddy.API.url import AddyURL


class AliasBulkActions:
    def __init__(self) -> None:
        self.url = AddyURL()
        self.api_key = AddyKey().load_key()

    def _build_payload(self, ids: list[str]) -> dict:
        payload = {"ids": ids}
        return payload

    def get_aliases(
        self,
        ids: list[str],
    ):
        """Get detailed info on aliases list"""

        response = requests.request(
            "POST",
            self.url.bulk_get_aliases(),
            headers=self.url.get_headers(self.api_key),
            json=self._build_payload(ids),
        )

        return response

    def bulk_activate_aliases(self, ids: list[str]):
        """Bulk activate list of aliases"""

        response = requests.request(
            "POST",
            self.url.bulk_activate_aliases(),
            headers=self.url.get_headers(self.api_key),
            json=self._build_payload(ids),
        )

        return response

    def bulk_deactivate_aliases(self, ids: list[str]):
        """Bulk deactivate list of aliases"""

        response = requests.request(
            "POST",
            self.url.bulk_deactivate_aliases(),
            headers=self.url.get_headers(self.api_key),
            json=self._build_payload(ids),
        )

        return response

    def bulk_deleted_aliases(self, ids: list[str]):
        """Bulk deleted list of aliases"""

        response = requests.request(
            "POST",
            self.url.bulk_delete_aliases(),
            headers=self.url.get_headers(self.api_key),
            json=self._build_payload(ids),
        )

        return response

    def bulk_restore_aliases(self, ids: list[str]):
        """Bulk restore list of aliases"""

        response = requests.request(
            "POST",
            self.url.bulk_restore_aliases(),
            headers=self.url.get_headers(self.api_key),
            json=self._build_payload(ids),
        )

        return response

    def bulk_forget_aliases(self, ids: list[str]):
        """Bulk forget list of aliases"""

        response = requests.request(
            "POST",
            self.url.bulk_forget_aliases(),
            headers=self.url.get_headers(self.api_key),
            json=self._build_payload(ids),
        )

        return response
