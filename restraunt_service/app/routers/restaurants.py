from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/restaurants", tags=["restaurants"])

@router.post("/", response_model=schemas.RestaurantResponse)
async def create_restaurant(restaurant: schemas.RestaurantBase, db: Session = Depends(database.get_db)):
    return crud.create_restaurant(db, restaurant.dict())

@router.put("/{restaurant_id}", response_model=schemas.RestaurantResponse)
async def update_restaurant(restaurant_id: int, updates: schemas.RestaurantUpdate, db: Session = Depends(database.get_db)):
    db_restaurant = crud.update_restaurant(db, restaurant_id, updates.dict(exclude_unset=True))
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant
