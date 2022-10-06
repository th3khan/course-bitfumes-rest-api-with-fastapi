from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .schemas import BlogRequest
from .models  import Blog
from database  import get_db

blog_router = APIRouter(prefix='/blog', tags=['Blog'])

@blog_router.get('/')
def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@blog_router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not exist.')
    return blog

@blog_router.get('/{id}/comments')
def comments(id: int, limit: int):
    return {
        'data': f'Get {limit} comment from blog with id: {id}'
    }

@blog_router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogRequest, db: Session = Depends(get_db)):
    new_blog = Blog(title=blog.title, body=blog.body)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@blog_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(detail='Blog not Exists', status_code=404)
    
    db.query(Blog).filter(Blog.id == id).delete()
    db.commit()
    return

@blog_router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id: int, request: BlogRequest,  db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(detail='Blog not Exists', status_code=404)
    
    db.query(Blog).filter(Blog.id == id).update({
        'title': request.title,
        'body': request.body
    })
    db.commit()
    return {
        'data': 'Blog updated successfully'
    }
