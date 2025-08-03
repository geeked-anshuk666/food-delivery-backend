from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from .. import schemas, crud, database, models

router = APIRouter(prefix="/delivery-agents", tags=["delivery-agents"])

@router.post("/assign", response_model=schemas.DeliveryAgentAssignment)
async def assign_delivery_agent(
    assignment_data: Dict[str, Any],
    db: Session = Depends(database.get_db)
):
    """Assign an available delivery agent to an order"""
    order_id = assignment_data.get("order_id")
    restaurant_id = assignment_data.get("restaurant_id")
    
    if not order_id or not restaurant_id:
        raise HTTPException(status_code=400, detail="Missing order_id or restaurant_id")
    
    # Find an available delivery agent
    available_agents = crud.get_available_agents(db)
    
    if not available_agents:
        # Return a more specific error message
        raise HTTPException(status_code=404, detail="No delivery agents available")
    
    # Select the first available agent
    available_agent = available_agents[0]
    
    # Mark the agent as unavailable
    available_agent.is_available = False
    available_agent.current_order_id = order_id
    db.commit()
    db.refresh(available_agent)
    
    return {"delivery_agent_id": available_agent.id, "order_id": order_id}