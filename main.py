from fastapi import FastAPI
from config.settings import settings
from config.database import engine, Base

# Import routes to register them
from users import routes as users_routes
from auth import routes as auth_routes
from blog import routes as blog_routes
from comments import routes as comments_routes

# Import models to ensure they are registered with Base metadata
from users import models as user_models
from blog import models as blog_models
from comments import models as comment_models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth_routes.router, prefix=settings.API_V1_STR)
app.include_router(users_routes.router, prefix=settings.API_V1_STR)
app.include_router(blog_routes.router, prefix=settings.API_V1_STR)
app.include_router(comments_routes.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Feature Based App"}
