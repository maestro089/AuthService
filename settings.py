from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRETE_KEY: str

    @property
    def sqlite_url_syncpg(self):
        return f"sqlite:///auth.db"

    class Config:
        env_file = ".env"


settings = Settings()
