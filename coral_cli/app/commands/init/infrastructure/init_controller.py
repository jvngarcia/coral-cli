from ..domain.interfaces import IEstructureCreator, IInitRepository
from ..application.structure_creator import StructureCreator
from .os_project_init_repository import OsProjectInitRepository


class InitController():
  def __init__(self):
    repository: IInitRepository = OsProjectInitRepository()
    self.init_service: IEstructureCreator = StructureCreator(repository)

  def run(self, name: str, description: str):
    return self.init_service.run(
      name=name,
      description=description
    )