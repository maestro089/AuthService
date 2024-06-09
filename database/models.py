from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String),
    Column('email', String),
    Column('password', String),
)
