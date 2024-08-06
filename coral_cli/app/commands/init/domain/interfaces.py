from abc import ABC
from .vo import Project

class IInitRepository(ABC):
    def create(self, project: Project):
      pass

class IEstructureCreator(ABC):
  
  def __init__(self, repository: IInitRepository) -> None:
    pass
  
  def run(self, name: str, description: str):
    pass