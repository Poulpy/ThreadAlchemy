from fastapi import APIRouter, FastAPI, HTTPException, status

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/health")
def health():
    return {"Status": "OK"}
