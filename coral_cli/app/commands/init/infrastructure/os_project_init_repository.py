
from ..domain.interfaces import IInitRepository
from ..domain.vo import Project, ProjectName
from ..application.structure_builder import StructureBuilder
import os

class OsProjectInitRepository(IInitRepository):
  
  def __init__(self) -> None:
    self.builder = StructureBuilder()
  
  def create(self, project: Project):
    self.assure_exists(project.name)
    
    with open(f'{project.name.value.value}/main.py', 'w') as f:
      f.write(self.builder.archive(project))

  def assure_exists(self, name: ProjectName):
    if not os.path.exists(f"{name.value.value}/"):
      os.makedirs(f"{name.value.value}/")
      os.makedirs(f"{name.value.value}/commands/")
      os.makedirs(f"{name.value.value}/tests/")