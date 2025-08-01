from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/restaurants", tags=["restaurants"])

@router.get("/", response_model=list[schemas.RestaurantResponse])
async def get_online_restaurants(hour: int, db: Session = Depends(database.get_db)):
    if not 0 <= hour <= 23:
        raise HTTPException(status_code=400, detail="Invalid hour")
    restaurants = crud.get_online_restaurants(db, hour)
    return restaurants