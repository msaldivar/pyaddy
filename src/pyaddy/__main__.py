"""
Pyaddy

Maurice Saldivar

"""
import click
from addy import AddyApiDetails

@click.group()
@click.version_option("0.1.0", prog_name="Addy CLI")
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

if __name__ == "__main__":
    cli()