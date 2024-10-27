from typing import Optional
from passlib.hash import bcrypt
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"  

    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    books = relationship("Book", back_populates="owner") 
fake_users_db = {}

def create_user(username: str, password: str):
    hashed_password = bcrypt.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    fake_users_db[username] = user
    return user

def get_user(username: str) -> Optional[User]:
    return fake_users_db.get(username)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="books")