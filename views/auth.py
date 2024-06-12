import datetime

from fastapi import Depends, HTTPException
import jwt
from sqlalchemy import select

from db.models import Users, Tokens
from db.sqlite import get_session
from schemas.users import UserRegister
from settings import settings


class AuthView:
    def __init__(self, session=Depends(get_session)):
        self.session = session

    def _generate_token(self, userId: int) -> str:
        return jwt.encode(
            {
                "userId": userId,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            },
            settings.SECRETE_KEY,
            algorithm="HS256",
        )

    def _generate_fefresh_token(self, userId: int) -> str:
        return jwt.encode(
            {
                "userId": userId,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
            },
            settings.SECRETE_KEY,
            algorithm="HS256",
        )

    def _add_token(self, userId):
        newToken = Tokens.insert().values(
            UserID=userId,
            Token=self._generate_token(userId),
            RefreshToken=self._generate_fefresh_token(userId),
        )
        self.session.execute(newToken)
        self.session.commit()
        return {
            "token": self._generate_token(userId),
            "refreshToken": self._generate_fefresh_token(userId),
        }

    def register(self, data: UserRegister):
        existingUser = self.session.execute(
            select(Users).where(Users.c.Email == data.email)
        ).scalar()

        if existingUser:
            raise HTTPException(422, "Пользователь с таким Email уже существует")
        else:
            newUser = Users.insert().values(
                FirstName=data.firstName,
                LastName=data.lastName,
                Email=data.email,
                Password=data.password,
            )
            self.session.execute(newUser)
            self.session.commit()

            userId = self.session.execute(
                select(Users).where(Users.c.Email == data.email)
            ).first()

        return self._add_token(userId.id)
