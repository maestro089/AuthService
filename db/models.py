from sqlalchemy import (
    Column,
    Integer,
    String,
    MetaData,
    Table,
    DateTime,
    ForeignKey,
    Boolean,
    func,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

Users = Table(
    "Users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("FirstName", String),
    Column("LastName", String),
    Column("Email", String, unique=True),
    Column("Password", String),
    Column("DateCreated", DateTime, default=func.now()),
    Column("DateLastVisited", DateTime, default=func.now()),
    Column("Active", Boolean, default=True),
)


Tokens = Table(
    "Tokens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("UserID", ForeignKey("Users.id")),
    Column("Token", String, default=""),
    Column("RefreshToken", String, default=""),
    Column("DateCreated", DateTime, default=func.now()),
    Column("DateUpdate", DateTime, onupdate=func.now()),
)
