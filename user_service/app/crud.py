from sqlalchemy.orm import Session
from . import models
from datetime import datetime

def get_online_restaurants(db: Session, hour: int):
    return db.query(models.Restaurant).filter(models.Restaurant.is_online == True).all()

def create_order(db: Session, order: dict):
    db_order = models.Order(
        user_id=order["user_id"],
        restaurant_id=order["restaurant_id"],
        status="pending",
        created_at=datetime.utcnow()
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def create_rating(db: Session, rating: dict, user_id: int):
    db_rating = models.Rating(
        user_id=user_id,
        order_id=rating["order_id"],
        restaurant_rating=rating["restaurant_rating"],
        delivery_rating=rating["delivery_rating"]
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def create_user(db: Session, user: dict):
    db_user = models.User(email=user["email"])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
