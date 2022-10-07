from pydantic import BaseModel

class UserBase(BaseModel):

    email: str
    password: str
    name: str

class UserResponse(UserBase):
    id: int

    class Config():
        orm_mode = True

class UserRequest(UserBase):
    pass