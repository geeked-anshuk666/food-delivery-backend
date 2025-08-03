from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models
import httpx

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/{order_id}/assign", response_model=schemas.OrderResponse)
async def assign_delivery_agent(order_id: int, db: Session = Depends(database.get_db)):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://delivery-service:8003/agents/available")
        # response = await client.get("http://localhost:8003/agents/available")
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="No available agents")
        agents = response.json()
        if not agents:
            raise HTTPException(status_code=400, detail="No available agents")
        order = crud.assign_delivery_agent(db, order_id, agents[0]["id"])
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

@router.put("/{order_id}/status", response_model=schemas.OrderResponse)
async def update_order_status(order_id: int, status: str, db: Session = Depends(database.get_db)):
    if status not in ["accepted", "rejected", "preparing"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    order = crud.update_order_status(db, order_id, status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
