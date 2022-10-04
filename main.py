from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        'api': 'v1'
    }

@app.get('/blog')
def get_blog(limit: int, publised: bool = True, sort: Optional[str] = None):
    if publised:
        return { 'data': f'{limit} blog list PUBLISHED' }
    else:
        return { 'data': f'{limit} blog list UNPUBLISHED' }

@app.get('/blog/{id}')
def get_blog(id: int):
    return { 'data' : id }

@app.get('/blog/{id}/comments')
def comments(id: int, limit: int):
    return {
        'data': f'Get {limit} comment from blog with id: {id}'
    }