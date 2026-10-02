from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from enum import Enum
from random import randint

class Category(Enum):
    SEWING = 0
    KNITTING = 1
    CROCHET = 2
    TATTING = 3
    LACE = 4
    EMBROIDERY = 5
    CROSS_STITCH = 6
    WEAVING = 7
    MACRAME = 8
    SPINNING = 9
    FELTING = 10

class Difficulty(Enum):
    BEGINNER = 0
    INTERMEDIATE = 1
    EXPERT = 2

class Project(BaseModel):
    id: str
    name: str
    description: str | None = ""
    category: Category
    difficulty: Difficulty | None = Difficulty.BEGINNER

class ProjectCreate(BaseModel):
    name: str
    description: str | None = ""
    category: Category
    difficulty: Difficulty | None = Difficulty.BEGINNER

    def build(self):
        id = str(randint(1, 10000))
        return Project(id = id, name = self.name, description = self.description, category = self.category, difficulty = self.difficulty)


app = FastAPI()
projects = [Project(id="1", name= "Casquette", category= Category.SEWING)]


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health():
    return {"Status": "OK"}

@app.get("/projects")
def read_projects():
    return projects

@app.post("/projects", status_code=status.HTTP_201_CREATED)
def create_project(project_dummy: ProjectCreate):
    projects.append(project_dummy.build())
    print(projects)
    print(projects[0])
    print(projects[1])
    return projects[-1]

@app.get("/projects/{project_id}", status_code=200)
def read_project(project_id: str, response: Response):
    project = list(filter(lambda x: x.id == project_id, projects))
    if len(project) == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        return project

