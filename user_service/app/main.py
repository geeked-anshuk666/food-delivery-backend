from fastapi import FastAPI
from .routers import users, restaurants, orders
from . import models, database

app = FastAPI(
    title="User Service API",
    description="API for user management in the food delivery system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers
app.include_router(users.router)
app.include_router(restaurants.router)
app.include_router(orders.router)

# Create tables
models.Base.metadata.create_all(bind=database.engine)
