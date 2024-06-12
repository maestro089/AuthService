from fastapi import APIRouter

from db.models import Users

auth = APIRouter()


@auth.get("/")
async def home():
    return {"message": "Hello World"}
