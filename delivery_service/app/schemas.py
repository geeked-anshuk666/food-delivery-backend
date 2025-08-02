from pydantic import BaseModel
from typing import Optional

class DeliveryAgentBase(BaseModel):
    name: str
    is_available: bool

class DeliveryAgentResponse(DeliveryAgentBase):
    id: int
    class Config:
        from_attributes=True