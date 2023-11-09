"""
Class for the base addy url.

if a change is made to the url path, make change here so none of the classes
need to explicity now the api path  

"""

class AddyURL:

    def __init__(self) -> None:
        self.base_url = 'https://app.addy.io/api/v1/{}'

    

    def api_details(self) -> str:
        return self.base_url.format('api-token-details')
    
    def account_details(self) -> str:
        return self.base_url.format('account-details')
    
    def bulk_get_aliases(self) -> str:
        return self.base_url.format('aliases/get/bulk')
    
    def bulk_activate_aliases(self) -> str:
        return self.base_url.format('aliases/activate/bulk')
    
    def bulk_deactivate_aliases(self) -> str:
        return self.base_url.format('aliases/deactivate/bulk')
    
    def bulk_delete_aliases(self) -> str:
        return self.base_url.format('aliases/delete/bulk')
    
    def bulk_restore_aliases(self) -> str:
        return self.base_url.format('aliases/restore/bulk')
    
    def bulk_forget_aliases(self) -> str:
        return self.base_url.format('aliases/forget/bulk')
    
    def bulk_update_recipients_for_aliases(self) -> str:
        return self.base_url.format('aliases/recipients/bulk')
    