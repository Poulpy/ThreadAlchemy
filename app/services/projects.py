from uuid import uuid4

from pydantic import BaseModel

from ..schema.models.project import Category, Difficulty, Project


class ProjectCreate(BaseModel):
    name: str
    description: str | None = ""
    category: Category
    difficulty: Difficulty | None = Difficulty.BEGINNER

    def build(self):
        id = str(uuid4())
        return Project(
            id=id,
            name=self.name,
            description=self.description,
            category=self.category,
            difficulty=self.difficulty,
        )
