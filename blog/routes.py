from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from .schemas import BlogRequest
from .models  import Blog
from database  import get_db

blog_router = APIRouter(prefix='/blog', tags=['Blog'])

@blog_router.get('/')
def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@blog_router.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'Blog not exist.'}
    return blog

@blog_router.get('/blog/{id}/comments')
def comments(id: int, limit: int):
    return {
        'data': f'Get {limit} comment from blog with id: {id}'
    }

@blog_router.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogRequest, db: Session = Depends(get_db)):
    new_blog = Blog(title=blog.title, body=blog.body)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog