"""
Pyaddy - cli for addy api

Maurice Saldivar
"""
import click
from click.core import Context
from click.formatting import HelpFormatter
from pyaddy.API.addy_key import AddyKey
from pyaddy.commands import alias_bulk_actions_cmd as bulk_alias
from pyaddy.commands import aliases_cmd as aliases
from pyaddy.commands import api_details_cmd as api_details


class CliGroup(click.Group):
    def format_usage(self, ctx: Context, formatter: HelpFormatter) -> None:
        click.echo("Usage: addy <command> <subcommand> [options & parameters]\n")


@click.group(cls=CliGroup)
@click.version_option("0.5.2", prog_name="Addy CLI")
def cli():
    """CLI tool to interact with addy.io api:\n
    
    Run load_key first to add api key:

    addy load_ley <key goes here>
    """
    pass


@cli.command(name="load-key")
@click.argument("key", type=str)
def load_key(key) -> None:
    """Load api key. 
    
    KEY api key
    """
    AddyKey().write_to_config(key)
    click.echo('Key saved')


# api details cmds
cli.add_command(api_details.api)

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
