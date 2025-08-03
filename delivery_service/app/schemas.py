from pydantic import BaseModel
from typing import Optional

class DeliveryAgentBase(BaseModel):
    name: str
    is_available: bool

class DeliveryAgentResponse(DeliveryAgentBase):
    id: int
    class Config:
        from_attributes=True


class DeliveryAgentAssignment(BaseModel):
    delivery_agent_id: int
    order_id: int
    
    class Config:
        from_attributes = True