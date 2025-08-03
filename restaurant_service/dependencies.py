from shared.service_client import ServiceClient
from shared.config import USER_SERVICE_URL, DELIVERY_AGENT_SERVICE_URL

# Create clients for other services
user_service = ServiceClient(USER_SERVICE_URL)
delivery_service = ServiceClient(DELIVERY_AGENT_SERVICE_URL)