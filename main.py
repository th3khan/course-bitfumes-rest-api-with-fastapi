from fastapi import FastAPI
from blog.routes import blog_router
from blog import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog_router)

@app.get('/')
def index():
    return {
        'api': 'v1'
    }