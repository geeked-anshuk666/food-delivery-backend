from shared.service_client import ServiceClient
from shared.config import RESTAURANT_SERVICE_URL, DELIVERY_AGENT_SERVICE_URL

# Create clients for other services
restaurant_service = ServiceClient(RESTAURANT_SERVICE_URL)
delivery_service = ServiceClient(DELIVERY_AGENT_SERVICE_URL)