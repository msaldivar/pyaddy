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


