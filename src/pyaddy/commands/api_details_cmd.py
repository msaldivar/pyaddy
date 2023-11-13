"""
Click cmds for the AddyApiDetails class
"""


import click
import json
from pyaddy.API.api_details import AddyApiDetails

@click.command(name='get-api-details', help='Get api details to confirm key is valid')
def check_api_key_details():
    """Check the details of the api key"""
    resp = AddyApiDetails().get_api_details()

    click.echo(f'API details: {json.dumps(resp.json(), indent=4)}')

@click.command(name="get-account-details", short_help="Get all account details associated with api key")
def get_account_details():
    """Get all account details associated with api key"""
    resp = AddyApiDetails().get_account_details()

    click.echo(f'Account Details: \n {json.dumps(resp.json(), indent=4)}')