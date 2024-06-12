from sqlalchemy import Column, Integer, String, MetaData, Table, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

Users = Table(
    "Users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("FirstName", String),
    Column("LastName", String),
    Column("Email", String),
    Column("Password", String),
    Column("DateCreated", DateTime),
    Column("DateLastVisited", DateTime),
)


Tokens = Table(
    "Tokens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("UserID", ForeignKey("Users.id")),
    Column("Token", String),
    Column("RefreshToken", String),
    Column("DateCreated", DateTime),
)
