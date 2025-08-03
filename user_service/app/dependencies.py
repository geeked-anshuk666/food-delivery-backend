from sqlalchemy.orm import Session
from . import database
import sys
import os

# Add the parent directory to sys.path to find the shared module
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from shared.service_client import ServiceClient
from shared.config import RESTAURANT_SERVICE_URL, DELIVERY_AGENT_SERVICE_URL

# Create clients for other services
restaurant_service = ServiceClient(RESTAURANT_SERVICE_URL)
delivery_service = ServiceClient(DELIVERY_AGENT_SERVICE_URL)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()