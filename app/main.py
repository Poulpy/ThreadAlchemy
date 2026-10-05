from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from .db import engine
from .routers import misc, projects


@asynccontextmanager
async def lifespan(app: FastAPI):
    # vérifie la connexion au démarrage : échoue vite si la base est injoignable
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(misc.router)
app.include_router(projects.router)
