from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, models

router = APIRouter(prefix="/menu", tags=["menu"])

@router.post("/{restaurant_id}", response_model=schemas.MenuItemResponse)
async def create_menu_item(restaurant_id: int, menu_item: schemas.MenuItemCreate, db: Session = Depends(database.get_db)):
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.create_menu_item(db, menu_item.dict(), restaurant_id)