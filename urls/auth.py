from fastapi import APIRouter, Depends

from db.models import Users
from schemas.users import UserRegister
from views.auth import AuthView

auth = APIRouter()


@auth.get("/")
async def home():
    return {"message": "Hello World"}


@auth.post("/register")
def register(
    data: UserRegister,
    services: AuthView = Depends(),
):
    return services.register(data=data)
