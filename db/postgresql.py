from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import String, create_engine
from settings import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_PSYCOPG,
    echo=True,
)

Session = sessionmaker(
    sync_engine,
    autocommit=False,
    autoflush=False,
)

def get_session_postgres():
    session = Session()
    try:
        yield session
    finally:
        session.close()
