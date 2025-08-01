from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class DeliveryAgent(Base):
    __tablename__ = "delivery_agents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_available = Column(Boolean)