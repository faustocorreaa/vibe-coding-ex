"""Test cases for the main application."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


# Create test client
client = TestClient(app)


class TestHealthEndpoints:
    """Test health check endpoints."""
    
    def test_root_endpoint(self):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "Welcome to Vibe Coding Extended API!" in data["message"]
        assert data["status"] == "healthy"
    
    def test_health_check(self):
        """Test the health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "timestamp" in data
        assert "version" in data


class TestGreetingEndpoints:
    """Test greeting endpoints."""
    
    def test_hello_world(self):
        """Test the hello world endpoint."""
        response = client.get("/api/v1/hello")
        assert response.status_code == 200
        data = response.json()
        assert "Hello World!" in data["message"]
        assert "timestamp" in data
        assert "vibe_level" in data
        assert "emoji" in data
    
    def test_personalized_greeting(self):
        """Test personalized greeting endpoint."""
        name = "Alice"
        response = client.get(f"/api/v1/hello/{name}")
        assert response.status_code == 200
        data = response.json()
        assert name in data["message"]
        assert data["name"] == name
        assert "fun_fact" in data
    
    def test_personalized_greeting_empty_name(self):
        """Test personalized greeting with empty name."""
        response = client.get("/api/v1/hello/   ")
        assert response.status_code == 400
    
    def test_personalized_greeting_long_name(self):
        """Test personalized greeting with very long name."""
        long_name = "a" * 60
        response = client.get(f"/api/v1/hello/{long_name}")
        assert response.status_code == 400
    
    def test_random_greeting(self):
        """Test random greeting endpoint."""
        response = client.get("/api/v1/greetings/random")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "timestamp" in data
        assert "vibe_level" in data
    
    def test_greeting_stats(self):
        """Test greeting statistics endpoint."""
        response = client.get("/api/v1/greetings/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_vibe_levels" in data
        assert "total_emojis" in data
        assert "available_endpoints" in data
        assert data["vibe_energy"] == "Maximum! 🔥"


class TestMiddleware:
    """Test custom middleware."""
    
    def test_process_time_header(self):
        """Test that process time header is added."""
        response = client.get("/")
        assert "X-Process-Time" in response.headers
        assert "X-Powered-By" in response.headers
        assert "Vibe-Coding-Extended" in response.headers["X-Powered-By"]


# Example parametrized test
@pytest.mark.parametrize("name,expected_status", [
    ("John", 200),
    ("Alice", 200),
    ("Bob123", 200),
    ("", 404),  # Empty string in URL becomes 404
])
def test_greeting_with_various_names(name, expected_status):
    """Test greeting endpoint with various names."""
    if name:
        response = client.get(f"/api/v1/hello/{name}")
    else:
        response = client.get("/api/v1/hello/")
    
    assert response.status_code == expected_status