from dataclasses import dataclass

@dataclass
class ProjectName():
  value: str
  
@dataclass
class ProjectDescription():
  value: str
  
@dataclass
class Project:
  name: ProjectName
  description: ProjectDescription
  
  @staticmethod
  def create(name: str, description: str):
    return Project(ProjectName(name), ProjectDescription(description))
  
  def __str__(self):
    return f'Project: {self.name.value} - {self.description.value}'