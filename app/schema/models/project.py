from enum import Enum

from pydantic import BaseModel


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
    FELTING = "felting"


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
