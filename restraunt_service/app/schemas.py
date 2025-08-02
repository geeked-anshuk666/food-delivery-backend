from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    price: float

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemResponse(MenuItemBase):
    id: int
    restaurant_id: int
    class Config:
        orm_mode = True

class RestaurantBase(BaseModel):
    name: str
    is_online: bool

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    is_online: Optional[bool] = None

class RestaurantResponse(RestaurantBase):
    id: int
    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    restaurant_id: int
    delivery_agent_id: Optional[int]
    status: str
    class Config:
        orm_mode = True
