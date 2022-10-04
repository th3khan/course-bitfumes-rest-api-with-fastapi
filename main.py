from fastapi import FastAPI
from blog.routes import blog_router

app = FastAPI()

app.include_router(blog_router)

@app.get('/')
def index():
    return {
        'api': 'v1'
    }