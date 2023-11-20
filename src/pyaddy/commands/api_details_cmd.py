"""
Click cmds for the AddyApiDetails class
"""


import click
import json
from pyaddy.API.api_details import AddyApiDetails


@click.group()
def api():
    """Invoke details about the provided api key"""


@api.command(name="api-details")
def check_api_key_details():
    """Check the details of the api key"""
    resp = AddyApiDetails().get_api_details()

    click.echo(f"API details: {json.dumps(resp.json(), indent=4)}")


@api.command(name="account-details")
def get_account_details():
    """Get all account details associated with api key"""
    resp = AddyApiDetails().get_account_details()

    click.echo(f"Account Details: \n {json.dumps(resp.json(), indent=4)}")
