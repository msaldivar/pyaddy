"""
Click cmds for the AliasBulkActions
"""

import click
import json
from pyaddy.API.alias_bulk_actions import AliasBulkActions


@click.command(name='get-bulk-aliases',
               short_help='Get detailed info on aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2')
@click.argument('ids', default=[])
def get_bulk_aliases(ids):
    """Get detailed info on aliases. Supply a comma-seperated list of alias IDs: 11111111-1111-1111-1111-111111111111,22222222-2222-2222-2222-222222222222
    """

    ids = ids.split(',')
    resp = AliasBulkActions().get_aliases(ids)

    click.echo(f'Detailed Aliases Info: \n {json.dumps(resp.json(), indent=4)}')


@click.command(name='bulk-activate-aliases',
               short_help='Bulk activate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2')
@click.argument('ids', default=[])
def bulk_activate_aliases(ids):
    """Bulk activate list of aliases"""

    ids = ids.split(',')
    resp = AliasBulkActions().bulk_activate_aliases(ids)

    click.echo(f'Bulk Activated Aliases Info: \n {json.dumps(resp.json(), indent=4)}')


@click.command(name='bulk-deactivate-aliases',
               short_help='Bulk deactivate list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2')
@click.argument('ids', default=[])
def bulk_deactivate_aliases(ids):
    """Bulk deactivate list of aliases"""

    ids = ids.split(',')
    resp = AliasBulkActions().bulk_deactivate_aliases(ids)

    click.echo(f'Bulk Deactivated Aliases Info: \n {json.dumps(resp.json(), indent=4)}')


@click.command(name='bulk-delete-aliases',
               short_help='Bulk delete list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2')
@click.argument('ids', default=[])
def bulk_delete_aliases(ids):
    """Bulk delete list of aliases"""

    ids = ids.split(',')
    resp = AliasBulkActions().bulk_deleted_aliases(ids)

    click.echo(f'Bulk Deleted Aliases Info: \n {json.dumps(resp.json(), indent=4)}')


@click.command(name='bulk-restore-aliases',
               short_help='Bulk restore list of aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2')
@click.argument('ids', default=[])
def bulk_restore_aliases(ids):
    """Bulk restore list of aliases"""

    ids = ids.split(',')
    resp = AliasBulkActions().bulk_restore_aliases(ids)

    click.echo(f'Bulk Restore Aliases Info: \n {json.dumps(resp.json(), indent=4)}')
