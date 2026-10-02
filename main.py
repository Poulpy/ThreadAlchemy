from fastapi import FastAPI, Response, HTTPException, status
from pydantic import BaseModel
from enum import Enum
from random import randint
from uuid import uuid4

class Category(Enum):
    SEWING = "sewing"
    KNITTING = "knitting"
    CROCHET = "crochet"
    TATTING = "tatting"
    LACE = "lace"
    EMBROIDERY = "embroidery"
    CROSS_STITCH = "cross_stitch"
    WEAVING = "weaving"
    MACRAME = "macrame"
    SPINNING = "spinning"
    FELTING = "1felting"

class Difficulty(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"

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
        id = str(uuid4())
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
    return projects[-1]

@app.get("/projects/{project_id}", status_code=200)
def read_project(project_id: str, response: Response):
    project = list(filter(lambda x: x.id == project_id, projects))
    if len(project) == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    else:
        return project[0]

