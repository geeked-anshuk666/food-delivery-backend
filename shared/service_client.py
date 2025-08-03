import requests
import json

class ServiceClient:
    """Client for making requests to other microservices"""
    
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
    
    def _make_url(self, endpoint):
        """Create a full URL from the endpoint"""
        endpoint = endpoint.lstrip('/')
        return f"{self.base_url}/{endpoint}"
    
    def get(self, endpoint, params=None):
        """Make a GET request to the service"""
        url = self._make_url(endpoint)
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data=None):
        """Make a POST request to the service"""
        url = self._make_url(endpoint)
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint, data=None):
        """Make a PUT request to the service"""
        url = self._make_url(endpoint)
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint):
        """Make a DELETE request to the service"""
        url = self._make_url(endpoint)
        response = requests.delete(url)
        response.raise_for_status()
        return response.json() if response.content else None