import asyncio

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings

sync_engine = create_engine(
    url="sqlite:///auth.db",
    echo=True,
)


Session = sessionmaker(
    sync_engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
