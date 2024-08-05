from string import Template
from ..domain.project import Project

class ProjectBuilder:
  def __init__(self) -> None:
    self.template = Template("""
import click

@click.command(name='$name', help='$description')
def cli_$name():
  click.echo("Hello World!")
      """)
  
  def archive(self, project: Project):    
    return self.template.substitute(name=project.name.value, description=project.description.value)