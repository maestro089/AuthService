from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
