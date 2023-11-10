"""
Click cmds for the AliasBulkActions
"""

import click
from pyaddy.API.alias_bulk_actions import AliasBulkActions

def split_ids(ctx, param, value):
    print(f'ctx: {ctx}')
    print(f'param: {param}')
    print(f'value: {value}')
    return ['1', '2', '4']

@click.command(name='get-bulk-aliases', short_help='Get detailed info on aliases. Supply a comma-seperated list of alias IDs -e.g. ID1, ID2')
@click.argument('ids', default=[])
def get_bulk_aliases(ids):
    """Get detailed info on aliases. Supply a comma-seperated list of alias IDs: 11111111-1111-1111-1111-111111111111,22222222-2222-2222-2222-222222222222
    """
    breakpoint()
    ids = ids.split(',')