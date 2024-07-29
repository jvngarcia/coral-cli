import click
import os
from string import Template


template = Template("""
# $name
# $description
import click

@click.command()
def cli():
  click.echo("Hello World!")

if __name__ == "__main__":
  cli()
""")


@click.command(name='init', help='init a CLI application')
@click.option('--name', '-n', help='Name of the project', required=True, type=click.STRING)
@click.option('--description', '-d', help='Description of the project', required=False, type=click.STRING)
def cli_init( name: str, description: str ):
  """
  Initialize your CLI application
  """
  click.echo(f'Initializing the CLI application: {name}')
  
  
  # Si no existe el directorio, lo creamos
  if not os.path.exists(name):
    os.makedirs(name)
  
  # Crear archivo main.py
  with open(f'{name}/main.py', 'w') as f:
    f.write(template.substitute(name=name, description=description))
  
  
  click.echo('Done!')