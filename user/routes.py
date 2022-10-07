import email
from unicodedata import name
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schemas import UserRequest, UserResponse
from .models import User
from database  import get_db
from helpers.hashing import Hash

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(request: UserRequest, db: Session = Depends(get_db)):
    userExists = db.query(User).where(User.email == request.email).first()

    if userExists:
        raise HTTPException(detail="Email user already is registered.", status_code=status.HTTP_400_BAD_REQUEST)

    
    new_user = User(name=request.name, email=request.email, password=Hash.bcrypy(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@user_router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
def create_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).where(User.id == id).first()

    if not user:
        raise HTTPException(detail="User not found.", status_code=status.HTTP_404_NOT_FOUND)

    return user