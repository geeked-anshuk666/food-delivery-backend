from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from ..dependencies import restaurant_service
from ..schemas import Restaurant

router = APIRouter()

@router.get("/restaurants/available", response_model=List[Restaurant])
async def get_available_restaurants():
    """Get all restaurants available at the current time"""
    current_hour = datetime.now().hour
    try:
        # Call restaurant service to get available restaurants
        restaurants = restaurant_service.get(
            "restaurants/available", 
            params={"hour": current_hour}
        )
        return restaurants
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Restaurant service unavailable: {str(e)}")