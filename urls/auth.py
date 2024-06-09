from fastapi import APIRouter

auth = APIRouter()


@auth.get("/")
async def home():
    return {"message": "Hello World"}
