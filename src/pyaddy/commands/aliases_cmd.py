"""
Click cmds for the Aliases class
"""

import click
import json
from pyaddy.API.aliases import Aliases


@click.command(name='get-all-aliases', short_help='Default: Get details about all ACTIVE aliases SORTED by CREATED_AT. --help to see all options and filtering')
@click.option('--only-ids', help='only show IDs', is_flag=True)
def get_all_aliases(only_ids):
    """Default: Get all ACTIVE aliases SORTED by CREATED_AT"""
    resp = Aliases().get_all_aliases()

    if only_ids:
        click.echo(f'Alias IDs:')
        [click.echo(aliases['id'] + ',', nl=False) for aliases in resp['data']]
        
    else:
        click.echo(f'All Aliases: \n {json.dumps(resp, indent=4)}')