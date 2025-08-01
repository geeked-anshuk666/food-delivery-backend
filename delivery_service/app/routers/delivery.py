from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/agents", tags=["delivery"])

@router.post("/", response_model=schemas.DeliveryAgentResponse)
async def create_delivery_agent(agent: schemas.DeliveryAgentBase, db: Session = Depends(database.get_db)):
    return crud.create_delivery_agent(db, agent.dict())

@router.get("/available", response_model=list[schemas.DeliveryAgentResponse])
async def get_available_agents(db: Session = Depends(database.get_db)):
    return crud.get_available_agents(db)

@router.put("/{agent_id}/status", response_model=schemas.DeliveryAgentResponse)
async def update_delivery_status(agent_id: int, is_available: bool, db: Session = Depends(database.get_db)):
    agent = crud.update_delivery_status(db, agent_id, is_available)
    if not agent:
        raise HTTPException(status_code=404, detail="Delivery agent not found")
    return agent