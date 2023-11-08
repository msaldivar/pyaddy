"""
Pyaddy

Maurice Saldivar

"""
import click
import json
from addy import AddyApiDetails

@click.group()
@click.version_option("0.2.0", prog_name="Addy CLI")
def cli():
    """Entry point for the cli"""
    pass

@cli.command(name="load-key", help="Supply your addy api-key")
@click.argument("key", type=str)
def load_key(key) -> None:
    """Grab the addy api key from the user"""
    with open("addy_key.cfg", "w") as f:
        f.write(key)

    click.echo(f"addy {key} saved to addy_key.cfg")

@cli.command(name="get-api-details", help="Get api details to confirm key is valid")
def check_api_key_details():
    """Check the details of the api key"""
    ac = AddyApiDetails()
    resp = ac.get_api_token_details()

    click.echo(f"API details: {resp}")

@cli.command(name="get-acount-details", help="Get all account details associated with api key")
def get_account_details():
    """Get all account details associated with api key"""
    ac = AddyApiDetails()
    resp = ac.get_account_details()

    click.echo(f"Account Details: \n {json.dumps(resp, indent=4)}")

if __name__ == "__main__":
    cli()