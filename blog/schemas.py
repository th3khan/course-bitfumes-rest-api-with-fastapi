from pydantic import BaseModel
from typing import Optional

class BlogRequest(BaseModel):
    title: str
    body: str
    published: Optional[bool]

class BlogResponse(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True