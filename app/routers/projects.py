import asyncio

from fastapi import APIRouter, HTTPException, status
from httpx import AsyncClient, ConnectError, HTTPStatusError, TimeoutException
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


@router.get("/{project_id}/prep")
async def prep_project(project_id: int, session: SessionDep):
    result = await session.get(ProjectModel, project_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Project not found")

    parameters = {"category": result.category.value, "difficulty": result.difficulty.value}
    async with AsyncClient() as client:
        try:
            a, b = await asyncio.gather(
                client.get("http://localhost:8000/furnitures", params=parameters),
                client.get("http://localhost:8000/tech_tips", params=parameters),
            )
            a.raise_for_status()
            b.raise_for_status()

            return {"furnitures": a.json(), "tips": b.json()}

        except TimeoutException as exc:
            raise HTTPException(status_code=504, detail="The materials service timed out") from exc
        except ConnectError as exc:
            raise HTTPException(status_code=502, detail="Connection timed out") from exc
        except HTTPStatusError as exc:
            raise HTTPException(status_code=502, detail="Status error: Connection error") from exc
