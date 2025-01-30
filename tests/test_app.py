import pytest
import sys
import os

# Add project directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Ensure this matches your renamed app file

@pytest.fixture
def client():
    """Create a test client for Flask app."""
    app.config["TESTING"] = True  # Enable testing mode
    with app.test_client() as client:
        yield client  # Provide the test client

def test_homepage(client):
    """Test the homepage route."""
    response = client.get("/")  # Simulate GET request
    assert response.status_code == 200  # Check if successful
    assert b"Hello, Flask World! I am Vicky!!!" in response.data  # Check response content
