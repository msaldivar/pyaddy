"""
Pyaddy

Maurice Saldivar

"""
import click
from pyaddy.API.addy import AddyApiDetails
from pyaddy.API.addy_key import AddyKey

@click.group()
@click.version_option("0.2.0", prog_name="Addy CLI")
def cli():
    """Entry point for the cli"""
    pass

@cli.command(name="load-key", help="Supply your addy api-key")
@click.argument("key", type=str)
def load_key(key) -> None:
    """Grab the addy api key from the user"""
    AddyKey().write_to_config(key)

    click.echo(f"Key saved")

@cli.command(name="get-api-details", help="Get api details to confirm key is valid")
def check_api_key_details():
    """Check the details of the api key"""
    resp = AddyApiDetails().get_api_details()

    click.echo(f"API details: {resp}")

@cli.command(name="get-account-details", help="Get all account details associated with api key")
def get_account_details():
    """Get all account details associated with api key"""
    resp = AddyApiDetails().get_account_details()

    click.echo(f"Account Details: \n {resp}")

if __name__ == "__main__":
    cli()