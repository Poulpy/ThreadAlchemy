from enum import Enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .schema.models.project import Category, Difficulty


def _values(enum_cls: type[Enum]) -> list[str]:
    return [m.value for m in enum_cls]  # stocke "sewing", pas "SEWING"


class Base(DeclarativeBase):
    pass


class ProjectModel(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(Text)
    category: Mapped[Category] = mapped_column(
        SAEnum(Category, values_callable=_values, native_enum=False)
    )
    difficulty: Mapped[Difficulty | None] = mapped_column(
        SAEnum(Difficulty, values_callable=_values, native_enum=False)
    )

    def __repr__(self) -> str:
        return f"Project(id={self.id!r}, "
        "name={self.name!r}, description={self.description!r}, category={self.category!r}, "
        "difficulty={self.difficulty!r})"
