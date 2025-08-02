from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models
import httpx

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schemas.OrderResponse)
async def place_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    restaurant = db.query(models.Restaurant).filter(
        models.Restaurant.id == order.restaurant_id,
        models.Restaurant.is_online == True
    ).first()
    if not restaurant:
        raise HTTPException(status_code=400, detail="Restaurant not available")
    db_order = crud.create_order(db, order.dict())
    async with httpx.AsyncClient() as client:
        # response = await client.post(f"http://restaurant-service:8002/orders/{db_order.id}/assign")
        response = await client.post(f"http://localhost:8002/orders/{db_order.id}/assign")
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to assign delivery agent")
    return db_order

@router.post("/ratings", response_model=schemas.RatingResponse)
async def create_rating(rating: schemas.RatingCreate, db: Session = Depends(database.get_db)):
    order = db.query(models.Order).filter(models.Order.id == rating.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not 0 <= rating.restaurant_rating <= 5 or not 0 <= rating.delivery_rating <= 5:
        raise HTTPException(status_code=400, detail="Ratings must be between 0 and 5")
    return crud.create_rating(db, rating.dict(), user_id=order.user_id)
