from sqlalchemy.orm import Session
from . import models
import requests

def create_menu_item(db: Session, menu_item: dict, restaurant_id: int):
    db_item = models.MenuItem(**menu_item, restaurant_id=restaurant_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_restaurant(db: Session, restaurant: dict):
    db_restaurant = models.Restaurant(**restaurant)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    try:
        response = requests.post(
            "http://user-service:8001/restaurants",
            json={"id": db_restaurant.id, "name": db_restaurant.name, "is_online": db_restaurant.is_online}
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to sync with user-service: {e}")
    return db_restaurant

def update_restaurant(db: Session, restaurant_id: int, updates: dict):
    db_restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if not db_restaurant:
        return None
    for key, value in updates.items():
        if value is not None:
            setattr(db_restaurant, key, value)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def update_order_status(db: Session, order_id: int, status: str):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        return None
    db_order.status = status
    db.commit()
    db.refresh(db_order)
    return db_order

def assign_delivery_agent(db: Session, order_id: int, agent_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        return None
    db_order.delivery_agent_id = agent_id
    db_order.status = "assigned"
    db.commit()
    db.refresh(db_order)
    return db_order
