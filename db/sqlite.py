import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import settings

async_engine = create_async_engine(
    url=settings.sqlite_url_asyncpg,
    echo=True,
)


Session = async_sessionmaker(
    async_engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
