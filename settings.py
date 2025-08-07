from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRETE_KEY: str

    @property
    def DATABASE_URL_PSYCOPG(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def SQLITE_URL_SYNCPG(self):
        return f"sqlite:///auth.db"

    class Config:
        env_file = ".env"


settings = Settings()
