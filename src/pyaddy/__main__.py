"""
Pyaddy - cli for addy api

Maurice Saldivar
"""
import click

from pyaddy.API.addy_key import AddyKey
from pyaddy.commands import api_details_cmd as api_details
from pyaddy.commands import alias_bulk_actions_cmd as bulk_alias
from pyaddy.commands import aliases_cmd as aliases

@click.group()
@click.version_option("0.5.0", prog_name="Addy CLI")
def cli():
    """Entry point for the cli"""
    pass

@cli.command(name="load-key", help="Supply your addy api-key")
@click.argument("key", type=str)
def load_key(key) -> None:
    """Grab the addy api key from the user"""
    AddyKey().write_to_config(key)

    click.echo(f'Key saved')

# api details cmds
cli.add_command(api_details.check_api_key_details)
cli.add_command(api_details.get_account_details)

# bulk cmds
cli.add_command(bulk_alias.get_bulk_aliases)
cli.add_command(bulk_alias.bulk_activate_aliases)
cli.add_command(bulk_alias.bulk_deactivate_aliases)
cli.add_command(bulk_alias.bulk_delete_aliases)
cli.add_command(bulk_alias.bulk_restore_aliases)

# aliases cmds
cli.add_command(aliases.get_all_aliases)
cli.add_command(aliases.get_specific_alias)
cli.add_command(aliases.create_new_alias)
cli.add_command(aliases.update_specific_alias)
cli.add_command(aliases.delete_specific_alias)
cli.add_command(aliases.forget_specific_alias)
cli.add_command(aliases.activate_alias)
cli.add_command(aliases.deactivate_alias)

if __name__ == "__main__":
    cli()