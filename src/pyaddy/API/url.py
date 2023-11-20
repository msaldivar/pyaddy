"""
Class for the base addy url.

if a change is made to the url path, make change here so none of the classes
need to explicity now the api path  

"""


class AddyURL:
    def __init__(self) -> None:
        self.base_url = "https://app.addy.io/api/v1/{}"

    def get_headers(self, api_key) -> dict:
        """Return headers used for request.

        Return:
            Dict[str]
        """

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
        }

        return headers

    def api_details(self) -> str:
        return self.base_url.format("api-token-details")

    def account_details(self) -> str:
        return self.base_url.format("account-details")

    def bulk_get_aliases(self) -> str:
        return self.base_url.format("aliases/get/bulk")

    def bulk_activate_aliases(self) -> str:
        return self.base_url.format("aliases/activate/bulk")

    def bulk_deactivate_aliases(self) -> str:
        return self.base_url.format("aliases/deactivate/bulk")

    def bulk_delete_aliases(self) -> str:
        return self.base_url.format("aliases/delete/bulk")

    def bulk_restore_aliases(self) -> str:
        return self.base_url.format("aliases/restore/bulk")

    def bulk_forget_aliases(self) -> str:
        return self.base_url.format("aliases/forget/bulk")

    def bulk_update_recipients_for_aliases(self) -> str:
        return self.base_url.format("aliases/recipients/bulk")

    def get_all_aliases(self) -> str:
        return self.base_url.format("aliases")

    def get_specific_alias(self) -> str:
        return self.base_url.format("aliases/{}")

    def create_new_alias(self) -> str:
        return self.base_url.format("aliases/")

    def restore_specific_alias(self) -> str:
        return self.base_url.format("aliases/{}/restore")

    def delete_alias(self) -> str:
        return self.base_url.format("aliases/{}")

    def forget_alias(self) -> str:
        return self.base_url.format("aliases/{}/forget")

    def activate_alias(self) -> str:
        return self.base_url.format("active-aliases")

    def deactivate_alias(self) -> str:
        return self.base_url.format("active-aliases/{}")
