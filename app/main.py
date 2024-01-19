from fastapi import FastAPI
from app.routers import url
from app.dependencies import mongodb

app = FastAPI()

# Include routers
app.include_router(url.router)

# Dependency for MongoDB connection
app.dependency_overrides[mongodb.get_database] = mongodb.get_database
