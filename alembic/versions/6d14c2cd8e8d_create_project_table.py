"""create project table

Revision ID: 6d14c2cd8e8d
Revises:
Create Date: 2026-10-05 10:49:46.043066

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6d14c2cd8e8d"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=False),
        sa.Column(
            "category",
            sa.Enum(
                "sewing",
                "knitting",
                "crochet",
                "tatting",
                "lace",
                "embroidery",
                "cross_stitch",
                "weaving",
                "macrame",
                "spinning",
                "felting",
                name="category",
                native_enum=False,
            ),
            nullable=False,
        ),
        sa.Column(
            "difficulty",
            sa.Enum(
                "beginner",
                "intermediate",
                "expert",
                name="difficulty",
                native_enum=False,
            ),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_projects")),
    )
    pass


def downgrade() -> None:
    op.drop_table("projects")
    pass
