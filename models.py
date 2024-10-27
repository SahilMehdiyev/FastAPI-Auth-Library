from typing import Optional
from pydantic import BaseModel
from passlib.hash import bcrypt


class User(BaseModel):
    username: str
    hashed_password: str
    
    def verify_password(self,password:str) -> bool:
        return bcrypt.verify(password, self.hashed_password)
    
fake_users_db = {}

def create_user(username: str, password: str):
    hashed_password = bcrypt.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    fake_users_db[username] = user
    return user

def get_user(username: str) -> Optional[User]:
    return fake_users_db.get(username)


    