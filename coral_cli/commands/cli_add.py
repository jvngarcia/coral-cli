import click
import os
from string import Template
from pathlib import Path
from ..app.commands.create.infrastructure.create_controller import CreateController


@click.command(name='add', help='Create a new command')
@click.option('--name', '-n', help='Name of the command', required=True, type=click.STRING)
@click.option('--description', '-d', help='Description of the project', required=False, type=click.STRING)
def cli_add(name: str, description: str):
  """
  Create a new command
  """
  click.echo(f'Creating a new command: {name}')
  controller = CreateController()
  controller.create(name, description)
  click.echo('Done!')
