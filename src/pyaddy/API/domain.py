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