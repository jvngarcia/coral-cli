from ..domain.create_repository import CreateRepository
from ..domain.project import Project
import os
from ..application.project_builder import ProjectBuilder

class OsProjectCreateRepository(CreateRepository):
  
  def __init__(self) -> None:
    self.dir = "./commands"
    self.template = ProjectBuilder()
  
  def generate(self, project: Project):
    self.assure_exists()
      
    with open(f'{self.dir}/cli_{project.name.value}.py', 'w') as f:
      f.write(self.template.archive(project))
  

  def assure_exists(self):
    if not os.path.exists(self.dir):
      os.makedirs(self.dir)