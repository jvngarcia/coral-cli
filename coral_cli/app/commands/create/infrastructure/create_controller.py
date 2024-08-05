from ..application.project_creator import ProjectCreator
from .os_project_create_repository import OsProjectCreateRepository

class CreateController:
    def __init__(self) -> None:
      repository = OsProjectCreateRepository()
      self.service = ProjectCreator(repository)

    def create(self, name: str, description: str):
      return self.service.create(name, description)