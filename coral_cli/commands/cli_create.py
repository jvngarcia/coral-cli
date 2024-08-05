import click
import os
from string import Template
from pathlib import Path
from ..app.commands.create.infrastructure.create_controller import CreateController

SUBCOMMAND_DIR = Path("coral_cli/commands")

template = Template("""
import click

@click.command(name='$name', help='$description')
def cli_$name():
  click.echo("Hello World!")

""")

template_group = Template("""
import click

@click.group(name='$name', help='$description')
def cli_$name():
  pass
  
@click.command(name='subcommand', help='None')
def cli_subcommand():
  click.echo('Subcommand')
  
""")

@click.group(name='create')
def cli_create():
  """
  Develop your CLI applications
  """
  pass



@cli_create.command(name='command', help='Create a new command')
@click.option('--name', '-n', help='Name of the command', required=True, type=click.STRING)
@click.option('--description', '-d', help='Description of the project', required=False, type=click.STRING)
def cli_command(name: str, description: str):
  """
  Create a new command
  """
  click.echo(f'Creating a new command: {name}')
  controller = CreateController()
  controller.create(name, description)
  click.echo('Done!')

@cli_create.command(name='group', help='Create a new group')
@click.option('--name', '-n', help='Name of the group', required=True, type=click.STRING)
@click.option('--description', '-d', help='Description of the project', required=False, type=click.STRING)
def cli_group(name: str, description: str):
  """
  Create a new group
  """
  
  click.echo(f'Creating a new group: {name}')
  
  # Si no existe el directorio, lo creamos
  if not os.path.exists(SUBCOMMAND_DIR):
    os.makedirs(SUBCOMMAND_DIR)
  
  # Crear archivo {name}.py
  with open(f'{SUBCOMMAND_DIR}/cli_{name}.py', 'w') as f:
    f.write(template_group.substitute(name=name, description=description))
  
  click.echo('Done!')
  
if __name__ == "__main__":
  cli_create()