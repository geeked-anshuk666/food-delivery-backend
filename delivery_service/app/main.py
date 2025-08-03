from fastapi import FastAPI
from .routers import delivery
from .database import engine
from . import models
import uvicorn

app = FastAPI(title="Delivery Agent Service")
models.Base.metadata.create_all(bind=engine)

app.include_router(delivery.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
