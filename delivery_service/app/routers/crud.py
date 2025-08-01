from sqlalchemy.orm import Session
from . import models

def get_available_agents(db: Session):
    return db.query(models.DeliveryAgent).filter(models.DeliveryAgent.is_available == True).all()

def update_delivery_status(db: Session, agent_id: int, is_available: bool):
    db_agent = db.query(models.DeliveryAgent).filter(models.DeliveryAgent.id == agent_id).first()
    if not db_agent:
        return None
    db_agent.is_available = is_available
    db.commit()
    db.refresh(db_agent)
    return db_agent

def create_delivery_agent(db: Session, agent: dict):
    db_agent = models.DeliveryAgent(**agent)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent