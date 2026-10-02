from fastapi import FastAPI

from .routers import misc, projects

app = FastAPI()

app.include_router(misc.router)
app.include_router(projects.router)
