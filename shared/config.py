import os

# Service URLs - default to localhost with the correct ports
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8001")
RESTAURANT_SERVICE_URL = os.getenv("RESTAURANT_SERVICE_URL", "http://localhost:8002")
DELIVERY_AGENT_SERVICE_URL = os.getenv("DELIVERY_AGENT_SERVICE_URL", "http://localhost:8003")