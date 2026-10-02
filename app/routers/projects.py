from fastapi import APIRouter, FastAPI, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

app = FastAPI()
projects = [Project(id="1", name= "Casquette", category= Category.SEWING)]

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)

@router.get("/")
def read_projects():
    return projects

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project(project_dummy: ProjectCreate):
    projects.append(project_dummy.build())
    return projects[-1]

@router.get("/{project_id}")
def read_project(project_id: str, response: Response):
    project = list(filter(lambda x: x.id == project_id, projects))
    if len(project) == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    else:
        return project[0]

