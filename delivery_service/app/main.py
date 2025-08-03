from fastapi import FastAPI
from .routers import delivery, delivery_agents
from . import models, database

app = FastAPI(
    title="Delivery Service API",
    description="API for delivery management in the food delivery system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers
app.include_router(delivery.router)
app.include_router(delivery_agents.router)

# Create tables
models.Base.metadata.create_all(bind=database.engine)
