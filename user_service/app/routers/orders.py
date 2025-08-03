from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models
from ..dependencies import restaurant_service, delivery_service
import logging

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    """Place a new order"""
    # Create the order in the database
    db_order = crud.create_order(db, order.dict())
    
    try:
        # Try to assign a delivery agent
        delivery_assignment = delivery_service.post(
            "delivery-agents/assign", 
            {
                "order_id": db_order.id,
                "restaurant_id": db_order.restaurant_id
            }
        )
        
        # Update the order with the delivery agent ID
        db_order.delivery_agent_id = delivery_assignment.get("delivery_agent_id")
        db.commit()
        db.refresh(db_order)
    except Exception as e:
        # If delivery agent assignment fails, just log the error but don't delete the order
        logging.error(f"Failed to assign delivery agent: {str(e)}")
        # The order will still be created without a delivery agent
    
    return db_order

@router.post("/ratings", response_model=schemas.RatingResponse)
async def create_rating(rating: schemas.RatingCreate, db: Session = Depends(database.get_db)):
    order = db.query(models.Order).filter(models.Order.id == rating.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not 0 <= rating.restaurant_rating <= 5 or not 0 <= rating.delivery_rating <= 5:
        raise HTTPException(status_code=400, detail="Ratings must be between 0 and 5")
    return crud.create_rating(db, rating.dict(), user_id=order.user_id)
