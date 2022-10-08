from pydantic import BaseModel
from typing import Optional

from user.schemas import UserResponse

class BlogRequest(BaseModel):
    title: str
    body: str
    published: Optional[bool]

class BlogResponse(BaseModel):
    title: str
    body: str
    author: UserResponse

    class Config():
        orm_mode = True