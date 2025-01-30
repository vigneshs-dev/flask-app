import pytest
import sys
import os
from flask import json

# Ensure Flask app is discoverable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Import the Flask app

@pytest.fixture
def client():
    """Create a test client for Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the homepage route"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Flask World! I am Vicky!!!" in response.data

def test_greet(client):
    """Test the greeting API"""
    response = client.get("/greet?name=Alice")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Alice!"}

    response = client.get("/greet")
    assert response.json == {"message": "Hello, Guest!"}

def test_add_numbers(client):
    """Test the addition API"""
    response = client.post("/add", json={"num1": 5, "num2": 7})
    assert response.status_code == 200
    assert response.json == {"result": 12.0}

    response = client.post("/add", json={"num1": "5.5", "num2": "2.5"})
    assert response.json == {"result": 8.0}

    response = client.post("/add", json={})  # Missing parameters
    assert response.status_code == 400
    assert "error" in response.json

    response = client.post("/add", json={"num1": "abc", "num2": 5})  # Invalid input
    assert response.status_code == 400
    assert "error" in response.json

def test_status(client):
    """Test the status API"""
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json == {"status": "running", "version": "1.0.0"}
