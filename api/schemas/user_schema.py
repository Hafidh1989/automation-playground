from typing import List

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    firstName: str
    lastName: str
    email: EmailStr
    username: str
    image: str


class UserListResponse(BaseModel):
    users: List[User]
    total: int
    skip: int
    limit: int