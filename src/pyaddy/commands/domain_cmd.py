"""
Click cmds for the Domain class
"""

import click
import json
from pyaddy.API.domain import Domain

@click.group()
def domain():
    """Invoke domain commands: --help for details

    addy domain <subcommand>
    """

@domain.command(name="all-options",
                short_help="retrieves all domain options")
def get_all_domain_options():
    """Retrieve all domain options"""

    resp = Domain().get_all_domain_options()
    click.echo(f"All Domain Options: \n {json.dumps(resp.json(), indent=4)}")

@domain.command(name="all",
                short_help="retrieves all domains")
def get_all_domains():
    """Retrieve all domains"""

    resp = Domain().get_all_domains()
    click.echo(f"All Domains: \n {json.dumps(resp.json(), indent=4)}")

@domain.command(name="get",
                short_help="get details of a specific domain ID")
@click.argument("id")
def get_specific_domain(id):
    """Get the details of a specific domain id
    
    Usage: \n
    addy domain get 0ad7a75a-1517-4b86-bb8a-9443d4965e60
    """

    resp = Domain().get_specific_domain(id)
    click.echo(f"All Domains: \n {json.dumps(resp.json(), indent=4)}")


@domain.command(name="create-new",
                short_help="create a new domain with the given NAME")
@click.argument("name")
def create_new_domain(name: str):
    """Create a new domain with the given NAME

    Usage: \n
    addy domain create-new example.com
    """

    payload = {"domain": name}
    resp = Domain().create_new_domain(payload)
    click.echo(f"Created Domain: \n {json.dumps(resp.json(), indent=4)}")