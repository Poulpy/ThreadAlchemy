from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from ..db import SessionDep
from ..db_models import ProjectModel
from ..schema.models.project import Project
from ..services.projects import ProjectCreate

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=list[Project])
async def read_projects(session: SessionDep):
    result = await session.scalars(select(ProjectModel))
    return result.all()


@router.post(
    "/",
    response_model=Project,
    response_model_exclude_unset=True,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(project: ProjectCreate, session: SessionDep):
    row = ProjectModel(**project.model_dump())
    session.add(row)
    await session.commit()
    await session.refresh(row)
    return row


@router.get("/{project_id}", response_model=Project, response_model_exclude_unset=True)
async def read_project(project_id: int, session: SessionDep):
    result = await session.get(ProjectModel, project_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return result
