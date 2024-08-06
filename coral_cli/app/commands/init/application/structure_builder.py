from string import Template
from ..domain.vo import Project

class StructureBuilder:
  def __init__(self) -> None:
    self.template = Template("""
import click
import importlib
from pathlib import Path
import re




SUBCOMMAND_DIR = Path("commands/")




@click.group()
def cli():
  pass

def add_subcommands(maincommand=cli):
  for modpath in SUBCOMMAND_DIR.glob('*.py'):
    modname = re.sub(f'/', '.',  str(modpath)).rpartition('.py')[0]
    
    # Replace backslash with dot
    modname = modname.replace('\\', '.')
    
    mod = importlib.import_module(modname)
    # Filter out any things that aren't a click Command
    for attr in dir(mod):
      foo = getattr(mod, attr)
      if callable(foo) and isinstance(foo, click.core.Command):
        maincommand.add_command(foo)


def init():
  add_subcommands()
  cli()""")
  
  def archive(self, project: Project):    
    return self.template.substitute(name=project.name.value, description=project.description.value)