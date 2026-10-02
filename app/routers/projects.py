from fastapi import APIRouter, HTTPException, status

from ..schema.models.project import Category, Project
from ..services.projects import ProjectCreate

router = APIRouter()

projects = [Project(id="1", name="Casquette", category=Category.SEWING)]

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/")
def read_projects():
    return projects


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate):
    projects.append(project.build())
    return projects[-1]


@router.get("/{project_id}")
def read_project(project_id: str):
    project = list(filter(lambda x: x.id == project_id, projects))
    if len(project) == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    else:
        return project[0]
