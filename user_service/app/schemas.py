from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class RestaurantBase(BaseModel):
    name: str
    is_online: bool

class RestaurantResponse(RestaurantBase):
    id: int
    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    item_id: int
    quantity: int

class OrderCreate(BaseModel):
    user_id: int
    restaurant_id: int
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: int
    user_id: int
    restaurant_id: int
    delivery_agent_id: Optional[int]
    status: str
    created_at: datetime
    class Config:
        orm_mode = True

class RatingCreate(BaseModel):
    order_id: int
    restaurant_rating: float
    delivery_rating: float

class RatingResponse(RatingCreate):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True