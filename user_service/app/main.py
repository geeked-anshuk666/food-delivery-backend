from fastapi import FastAPI
from .routers import users, restaurants, orders
from .database import engine
import uvicorn
from . import models

app = FastAPI(title="User Service")
models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(restaurants.router)
app.include_router(orders.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
