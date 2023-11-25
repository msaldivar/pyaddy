"""
Click cmds for the AliasBulkActions
"""

import click
import json
from pyaddy.API.alias_bulk_actions import AliasBulkActions


@click.group()
def bulk():
    """Invoke bulk alias commands: --help for details

    addy bulk <subcommand>
    """


@bulk.command(
    name="get-aliases",
    short_help="Get detailed info on aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
def get_bulk_aliases(ids):
    """Get detailed info on aliases.

    Supply a comma-seperated list of alias IDs:\n
    Usage:\n

    addy bulk get-aliases UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().get_aliases(ids)

    click.echo(f"Detailed Aliases Info: \n {json.dumps(resp.json(), indent=4)}")


@bulk.command(
    name="activate",
    short_help="Bulk activate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
def bulk_activate_aliases(ids):
    """Bulk activate list of aliases

    Supply a comma-seperated list of alias IDs:\n
    Usage:\n

    addy bulk activate UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_activate_aliases(ids)

    click.echo(f"Bulk Activated Aliases Info: \n {json.dumps(resp.json(), indent=4)}")


@bulk.command(
    name="deactivate",
    short_help="Bulk deactivate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
def bulk_deactivate_aliases(ids):
    """Bulk deactivate list of aliases

    Supply a comma-seperated list of alias IDs:\n
    Usage:\n

    addy bulk deactivate UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_deactivate_aliases(ids)

    click.echo(f"Bulk Deactivated Aliases Info: \n {json.dumps(resp.json(), indent=4)}")


@bulk.command(
    name="delete",
    short_help="Bulk delete list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
def bulk_delete_aliases(ids):
    """Bulk delete list of aliases

    Supply a comma-seperated list of alias IDs:\n
    Usage:\n

    addy bulk delete UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_deleted_aliases(ids)

    click.echo(f"Bulk Deleted Aliases Info: \n {json.dumps(resp.json(), indent=4)}")


@bulk.command(
    name="restore",
    short_help="Bulk restore list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1,ID2. --help for more info",
)
@click.argument("ids")
def bulk_restore_aliases(ids):
    """Bulk restore list of aliases

    Supply a comma-seperated list of alias IDs:\n
    Usage:\n

    addy bulk restore UUID-1,UUID-2,UUID-3
    """

    ids = ids.split(",")
    resp = AliasBulkActions().bulk_restore_aliases(ids)

    click.echo(f"Bulk Restore Aliases Info: \n {json.dumps(resp.json(), indent=4)}")
