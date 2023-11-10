"""
Class for all alias bulk actions
"""


import requests
import json

from pyaddy.API.url import AddyURL
from pyaddy.API.addy_key import AddyKey

class AliasBulkActions:

    def __init__(self) -> None:
        self.url = AddyURL()
        self.api_key = AddyKey().load_key()
    
    
    def get_aliases(self, ids: list[str]):
        """"""