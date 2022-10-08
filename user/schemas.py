from pydantic import BaseModel

class UserBase(BaseModel):

    email: str
    name: str

class UserResponse(UserBase):
    id: int

    class Config():
        orm_mode = True

class UserRequest(UserBase):
    password: str
    password_confirmation: str