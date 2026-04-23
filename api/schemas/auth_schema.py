from pydantic import BaseModel, EmailStr


class LoginResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    firstName: str
    lastName: str
    accessToken: str
    refreshToken: str