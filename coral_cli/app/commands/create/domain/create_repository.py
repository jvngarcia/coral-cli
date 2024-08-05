from abc import ABC
from .project import Project

class CreateRepository(ABC):

    def generate(self, project: Project):
        pass