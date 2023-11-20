"""
Click cmds for the Aliases class
"""

import click
import json
from pyaddy.API.aliases import Aliases


@click.group()
def alias():
    """Invoke alias commands: --help for details

    addy alias <subcommand>"""


@alias.command(
    name="get-all",
    short_help="Get details about all ACTIVE aliases SORTED by CREATED_AT. OPTION: --only-ids",
)
@click.option("--only-ids", help="only show IDs", is_flag=True)
def get_all_aliases(only_ids):
    """Get all aliases

    Default: Get all ACTIVE aliases SORTED by CREATED_AT:\n
    Usage:\n

    addy alias get-all\n
    addy alias get-all --only-ids
    """

    # TODO: look into filter options
    params = {
        "filter[active]": "true",
        "sort": "-created_at",
    }

    resp = Aliases().get_all_aliases(params)
    if only_ids:
        click.echo("Alias IDs:")
        [click.echo(aliases["id"] + ",", nl=False) for aliases in resp.json()["data"]]
        click.echo()
    else:
        click.echo(f"All Aliases: \n {json.dumps(resp.json(), indent=4)}")


@alias.command("get", short_help="Get ID details")
@click.argument("id")
def get_specific_alias(id):
    """Get ID details

    Usage:\n
    addy alias get UUID
    """

    resp = Aliases().get_specific_alias(id)
    click.echo(f"Alias Info: \n {json.dumps(resp.json(), indent=4)}")


@alias.command(name="new", short_help="Create a new alias. --help for all options")
@click.option(
    "--domain",
    help="the domain of the alias. Default addymail.com",
    default="addymail.com",
    type=str,
)
@click.option(
    "--description",
    help='the description of the alias. NOTE: put descripton in quotes "Descriptoin Foo Bar" ',
    type=str,
)
@click.option(
    "--format",
    help="chosen format for the alias: random_characters, uuid, or random_words",
    type=str,
)
@click.option(
    "--recipient-id",
    help="recipient id to add. Default recipient will be used if non is provided",
    type=str,
)
def create_new_alias(domain, description, format, recipient_id):
    """Create a new alias

    Usage:\n
    addy alias new

    addy alias new --domain addymail.com --description "addy created" --format random_words
    """

    payload = {
        "domain": domain,
        "description": description,
        "format": format,
        "recipient_id": recipient_id,
    }

    resp = Aliases().create_new_alias(payload)
    click.echo(f"Create New Alias Info: \n {json.dumps(resp.json(), indent=4)}")


@alias.command(name="update", short_help='Update alias "descprition" and "from_name"')
@click.argument("id")
@click.option(
    "--description",
    help='Updated DESCRIPTION: NOTE: put string in quotes: "PyAddy Update" Default: PyAddy Update',
    default="PyAddy Update",
)
@click.option(
    "--from-name",
    help='Updated FROM_NAME: NOTE: put string in quotes "Leonardo T." Default: Leonardo T.',
    default="Lenoardo T.",
)
def update_specific_alias(id, description, from_name):
    """Update alias "descprition" and "from_name"

    Usage:\n

    addy alias update UUID --description "foo addy" --from-name "bar addy"

    """

    payload = {"description": description, "from_me": from_name}

    resp = Aliases().update_specific_alias(id, payload)
    click.echo(f"Updated {id} Info: \n {json.dumps(resp.json(), indent=4)}")


@alias.command(name="restore", short_help="Restore alias ID")
@click.argument("id")
def restore_deleted_alias(id):
    """Restore an alias ID

    Usage:\n
    addy alias restore UUID
    """

    resp = Aliases().restore_specific_alias(id)
    click.echo(f"Restored {id} Info: \n {json.dumps(resp.json(), indent=4)}")


@alias.command(name="delete", short_help="Delete alias ID")
@click.argument("id")
def delete_specific_alias(id):
    """Delete an alias ID

    Usage:\n
    addy alias delete UUID
    """

    Aliases().delete_specific_alias(id)
    click.echo(f"Deleted {id}")


@alias.command(name="forget", short_help="Forget alias ID")
@click.argument("id")
def forget_specific_alias(id):
    """Forget an alias ID

    Usage:\n
    addy alias forget UUID
    """

    Aliases().forget_specific_alias(id)
    click.echo(f"Forgot {id}")


@alias.command(name="activate", short_help="Activate alias ID")
@click.argument("id")
def activate_alias(id):
    """Activate an alias ID

    Usage:\n
    addy alias activate UUID
    """

    payload = {"id": id}
    resp = Aliases().activate_alias(payload)
    click.echo(f"Activated {id} Info: \n {json.dumps(resp.json(), indent=4)}")


@alias.command(name="deactivate", short_help="Deactivate alias ID")
@click.argument("id")
def deactivate_alias(id):
    """Deactivate alias ID

    Usage:\n
    addy alias deactivate UUID
    """

    Aliases().deactivate_alias(id)
    click.echo(f"Deactivated {id}")
