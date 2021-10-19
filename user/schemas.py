from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    full_name: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    full_name: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
