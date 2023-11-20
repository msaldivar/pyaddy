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
    # TODO: look into filter options
    params = {
        'filter[active]': 'true',
        'sort': '-created_at',
    }

    resp = Aliases().get_all_aliases(params)
    if only_ids:
        click.echo('Alias IDs:')
        [click.echo(aliases['id'] + ',', nl=False) for aliases in resp.json()['data']]
        click.echo()
    else:
        click.echo(f'All Aliases: \n {json.dumps(resp.json(), indent=4)}')

@click.command(name='get-specific-alias', short_help='Get details about a specific alias')
@click.argument('id')
def get_specific_alias(id):
    """Get information about a specific alias"""

    resp = Aliases().get_specific_alias(id)
    click.echo(f'Alias Info: \n {json.dumps(resp.json(), indent=4)}')

@click.command(name='create-new-alias', short_help='see --help for all options')
@click.option('--domain', help='the domain of the alias. Default addymail.com', default='addymail.com', type=str)
@click.option('--description', help='the description of the alias. NOTE: put descripton in quotes "Descriptoin Foo Bar" ', type=str)
@click.option('--format', help='chosen format for the alias: random_characters, uuid, or random_words', type=str)
@click.option('--recipient-id', help='recipient id to add. Default recipient will be used if non is provided', type=str)
def create_new_alias(domain, description, format, recipient_id):
    """Create a new alias"""

    payload = {
        'domain': domain,
        'description': description,
        'format': format,
        'recipient_id': recipient_id
    }

    resp = Aliases().create_new_alias(payload)
    click.echo(f'Create New Alias Info: \n {json.dumps(resp.json(), indent=4)}')

@click.command(name='update-specific-alias', short_help='Update a specific alias descprition and from_name. Pass ID of alias')
@click.argument('id')
@click.option('--description', help='Updated description for the alias. NOTE: put descripton in quotes "PyAddy Update" Default: PyAddy Update', default='PyAddy Update')
@click.option('--from-name', help='Update from_name for alias. NOTE: put from_name in quotes "Leonardo T." Default: Leonardo T.', default='Lenoardo T.')
def update_specific_alias(id, description, from_name):
    """Update a specific alias descprition and from_name. Pass ID of alias"""

    payload = {
        'description': description,
        'from_me': from_name
    }

    resp = Aliases().update_specific_alias(id, payload)
    click.echo(f'Updated {id} Info: \n {json.dumps(resp.json(), indent=4)}')

@click.command(name='restore_deleted_alias', short_help='Restore a specific deleted alias. Pass ID of alias to retore')
@click.argument('id')
def restore_deleted_alias(id):
    """Restores a specific deleted alias"""

    resp = Aliases().restore_specific_alias(id)
    click.echo(f'Restored {id} Info: \n {json.dumps(resp.json(), indent=4)}')

@click.command(name='delete-specific-alias', short_help='Delete an alias. Pass ID of alias to delete')
@click.argument('id')
def delete_specific_alias(id):
    """Delete a specific alias"""

    Aliases().delete_specific_alias(id)
    click.echo(f'Deleted {id}')


@click.command(name='forget-specific-alias', short_help='Forget an alias. Pass ID of alias to forget')
@click.argument('id')
def forget_specific_alias(id):
    """Forget a specific alias"""

    Aliases().forget_specific_alias(id)
    click.echo(f'Forgot {id}')

@click.command(name='activate-alias', short_help='Activate an alias. Pass ID of alias to activate')
@click.argument('id')
def activate_alias(id):
    """Activate an alias"""

    payload = {
        'id': id
    }
    resp = Aliases().activate_alias(payload)
    click.echo(f'Activated {id} Info: \n {json.dumps(resp.json(), indent=4)}')

@click.command(name='deactivate-alias', short_help='Deactivate alias. Pass ID of alias to activate')
@click.argument('id')
def deactivate_alias(id):
    """Deactivate alias"""

    Aliases().deactivate_alias(id)
    click.echo(f'Deactivated {id}')
