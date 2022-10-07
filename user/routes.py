import email
from unicodedata import name
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

from .schemas import UserRequest, UserResponse
from .models import User
from database  import get_db

user_router = APIRouter(prefix='/users', tags=['Users'])

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

@user_router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(request: UserRequest, db: Session = Depends(get_db)):
    userExists = db.query(User).where(User.email == request.email).first()

    if userExists:
        raise HTTPException(detail="Email user already is registered.", status_code=status.HTTP_400_BAD_REQUEST)

    hashPassword = pwd_ctx.hash(request.password)
    new_user = User(name=request.name, email=request.email, password=hashPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user