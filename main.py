from fastapi import FastAPI
from blog.routes import blog_router
from user.routes import user_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog_router)
app.include_router(user_router)

@app.get('/')
def index():
    return {
        'api': 'v1'
    }