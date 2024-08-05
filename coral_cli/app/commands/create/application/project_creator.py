from ..domain.project import Project
from ..domain.create_repository import CreateRepository

class ProjectCreator:
  def __init__(self, repository: CreateRepository) -> None:
    self.repository = repository
  
  def create(self, name: str, description: str):
    project = Project.create(name, description)
    return self.repository.generate(project)