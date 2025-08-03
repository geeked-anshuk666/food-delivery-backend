from fastapi import FastAPI
from .routers import restaurants, menu, orders
from .database import engine
from . import models
import uvicorn

app = FastAPI(title="Restaurant Service")
models.Base.metadata.create_all(bind=engine)

app.include_router(restaurants.router)
app.include_router(menu.router)
app.include_router(orders.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
