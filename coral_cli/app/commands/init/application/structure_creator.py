from ..domain.interfaces import IEstructureCreator, IInitRepository
from ..domain.vo import Project, ProjectDescription, ProjectName

class StructureCreator(IEstructureCreator):
  def __init__(self, repository: IInitRepository) -> None:
    self.repository = repository
  
  def run(self, name: str, description: str):
    project = Project.create(ProjectName(name), ProjectDescription(description))
    return self.repository.create(project)