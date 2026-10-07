from fastapi import APIRouter

from ..schema.models.project import Category, Difficulty

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/health")
def health():
    return {"Status": "ok"}


@router.get("/furnitures")
def furnitures(category: Category, difficulty: Difficulty):
    match category:
        case Category.LACE:
            return ["fuseaux", "fils", "métiers (en polystyrène)", "aiguilles"]
        case Category.SEWING:
            return ["machines à coudre (22)", "tissus"]
        case _:
            return [""]


@router.get("/tech_tips")
def tech_tips(category: Category, difficulty: Difficulty):
    match category:
        case Category.LACE:
            return ["Ranger les métiers sur les étagères du haut"]
        case Category.SEWING:
            return ["Les machines sont dans le placard, la clef est à l'accueil"]
        case _:
            return [""]
