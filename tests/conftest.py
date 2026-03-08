import pytest
import copy
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Fixture providing FastAPI TestClient"""
    return TestClient(app)


@pytest.fixture
def fresh_activities(monkeypatch):
    """
    Fixture that provides fresh activities data for each test.
    Uses monkeypatch to replace the global activities dict with a clean copy.
    """
    # Create a deep copy of the original activities with clean state
    clean_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        }
    }
    
    # Replace the global activities with our clean copy
    monkeypatch.setattr("src.app.activities", clean_activities)
    return clean_activities


@pytest.fixture
def student_email():
    """Fixture providing a test student email"""
    return "newstudent@mergington.edu"


@pytest.fixture
def another_student_email():
    """Fixture providing another test student email"""
    return "another@mergington.edu"
