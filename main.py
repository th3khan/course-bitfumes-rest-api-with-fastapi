from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        'api': 'v1'
    }

@app.get('/blog')
def get_blog(limit: int):
    return { 'data': 'blog list' }

@app.get('/blog/{id}')
def get_blog(id: int):
    return { 'data' : id }