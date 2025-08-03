from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database, models
from ..dependencies import delivery_service

router = APIRouter(prefix="/orders", tags=["orders"])

@router.put("/{order_id}/accept", response_model=schemas.OrderResponse)
async def accept_order(order_id: int, db: Session = Depends(database.get_db)):
    """Accept an order and assign a delivery agent"""
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Update order status
    order.status = "accepted"
    db.commit()
    
    try:
        # Request a delivery agent from the delivery service
        delivery_assignment = delivery_service.post(
            "delivery-agents/assign", 
            {"order_id": order_id, "restaurant_id": order.restaurant_id}
        )
        
        # Update order with delivery agent info
        order.delivery_agent_id = delivery_assignment.get("delivery_agent_id")
        db.commit()
        db.refresh(order)
        
        return order
    except Exception as e:
        # Rollback in case of error
        order.status = "pending"
        db.commit()
        raise HTTPException(status_code=503, detail=f"Delivery service unavailable: {str(e)}")
