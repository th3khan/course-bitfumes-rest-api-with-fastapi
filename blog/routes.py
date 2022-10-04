from fastapi import APIRouter
from typing import Optional

from schemas import Blog

blog_router = APIRouter(prefix='/blog')

@blog_router.get('/')
def get_blog(limit: int, publised: bool = True, sort: Optional[str] = None):
    if publised:
        return { 'data': f'{limit} blog list PUBLISHED' }
    else:
        return { 'data': f'{limit} blog list UNPUBLISHED' }

@blog_router.get('/blog/{id}')
def get_blog(id: int):
    return { 'data' : id }

@blog_router.get('/blog/{id}/comments')
def comments(id: int, limit: int):
    return {
        'data': f'Get {limit} comment from blog with id: {id}'
    }

@blog_router.post('/blog')
def create_blog(blog: Blog):
    return {
        'data': f'Blog is created with title: {blog.title}'
    }