from fastapi import APIRouter, Depends, HTTPException
from ..database import get_db
from ..models import Restaurant
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/restaurants", tags=["restaurants"])

@router.get("/", response_model=list[schemas.RestaurantResponse])
async def get_online_restaurants(db: Session = Depends(database.get_db)):
    # if not 0 <= hour <= 23:
    #     raise HTTPException(status_code=400, detail="Invalid hour")
    restaurants = crud.get_online_restaurants(db)
    return restaurants

@router.post("/")
def create_restaurant(restaurant: dict, db: Session = Depends(get_db)):
    db_restaurant = Restaurant(**restaurant)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant