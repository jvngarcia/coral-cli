import click
import os
from string import Template
from coral_cli.app.commands.init.infrastructure.init_controller import InitController

@click.command(name='init', help='init a CLI application')
@click.option('--name', '-n', help='Name of the project', required=True, type=click.STRING)
@click.option('--description', '-d', help='Description of the project', required=False, type=click.STRING)
def cli_init( name: str, description: str ):
  """
  Initialize your CLI application
  """
  click.echo(f'Initializing the CLI application: {name}')
  controller = InitController()
  controller.run(name, description) 
  
  click.echo('Done!')