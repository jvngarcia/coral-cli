import click

@click.group()
def cli():
  """
  Develop your CLI applications
  """
  pass


def init():
  # Import all the commands here
  cli()
  
