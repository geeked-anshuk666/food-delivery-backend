from fastapi import FastAPI
from .routers import restaurants, orders, menu
from . import models, database

app = FastAPI(
    title="Restaurant Service API",
    description="API for restaurant management in the food delivery system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers
app.include_router(restaurants.router)
app.include_router(orders.router)
app.include_router(menu.router)  # Add this line to include the menu router

# Create tables
models.Base.metadata.create_all(bind=database.engine)
