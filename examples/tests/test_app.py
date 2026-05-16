"""
Mergington High School Activities API - Test Suite
EXAMPLE SOLUTION - Step 4 Completed

Comprehensive test suite using pytest and the AAA (Arrange-Act-Assert) pattern.
Tests all API endpoints and edge cases.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI application"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """
    Reset activities data before each test to ensure test isolation.
    This fixture runs automatically before each test.
    """
    activities.clear()
    activities.update({
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
        "Small Activity": {
            "description": "Test activity with limited capacity",
            "schedule": "Wednesdays, 3:00 PM - 4:00 PM",
            "max_participants": 2,
            "participants": ["test1@mergington.edu", "test2@mergington.edu"]
        }
    })
    yield
    # Cleanup after test (if needed)


# ============================================================================
# Root Endpoint Tests
# ============================================================================

def test_root_redirect(client):
    """Test that root endpoint redirects to static index page"""
    # Arrange - client fixture provides the test client
    
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307  # Temporary redirect
    assert response.headers["location"] == "/static/index.html"


# ============================================================================
# GET /activities Endpoint Tests
# ============================================================================

def test_get_activities_success(client):
    """Test GET /activities returns all activities"""
    # Arrange - activities set up in fixture
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert len(data) == 3


def test_get_activities_structure(client):
    """Test that activity objects have correct structure"""
    # Arrange - activities set up in fixture
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


# ============================================================================
# POST /activities/{activity_name}/signup Endpoint Tests
# ============================================================================

def test_signup_success(client):
    """Test successful signup for an activity"""
    # Arrange
    email = "newstudent@mergington.edu"
    activity_name = "Chess Club"
    initial_count = len(activities[activity_name]["participants"])
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert email in activities[activity_name]["participants"]
    assert len(activities[activity_name]["participants"]) == initial_count + 1
    assert "message" in response.json()


def test_signup_duplicate_prevention(client):
    """Test that duplicate signups are prevented (Bug fix from Step 2)"""
    # Arrange
    email = "michael@mergington.edu"  # Already signed up for Chess Club
    activity_name = "Chess Club"
    initial_count = len(activities[activity_name]["participants"])
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()
    assert len(activities[activity_name]["participants"]) == initial_count


def test_signup_nonexistent_activity(client):
    """Test signup for non-existent activity returns 404"""
    # Arrange
    email = "test@mergington.edu"
    activity_name = "Nonexistent Activity"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_signup_activity_full(client):
    """Test signup when activity is at max capacity"""
    # Arrange
    email = "newstudent@mergington.edu"
    activity_name = "Small Activity"  # Already has 2/2 participants
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "full" in response.json()["detail"].lower()


def test_signup_url_encoding(client):
    """Test signup with URL-encoded activity name"""
    # Arrange
    email = "test@mergington.edu"
    activity_name = "Programming Class"
    encoded_name = "Programming%20Class"
    
    # Act
    response = client.post(
        f"/activities/{encoded_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert email in activities[activity_name]["participants"]


# ============================================================================
# DELETE /activities/{activity_name}/signup Endpoint Tests (Step 3)
# ============================================================================

def test_unregister_success(client):
    """Test successful unregistration from an activity"""
    # Arrange
    email = "michael@mergington.edu"
    activity_name = "Chess Club"
    initial_count = len(activities[activity_name]["participants"])
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert len(activities[activity_name]["participants"]) == initial_count - 1
    assert "message" in response.json()


def test_unregister_not_signed_up(client):
    """Test unregistration when student is not signed up"""
    # Arrange
    email = "notsignedup@mergington.edu"
    activity_name = "Chess Club"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "not signed up" in response.json()["detail"].lower()


def test_unregister_nonexistent_activity(client):
    """Test unregistration from non-existent activity"""
    # Arrange
    email = "test@mergington.edu"
    activity_name = "Nonexistent Activity"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


# ============================================================================
# Integration Tests
# ============================================================================

def test_signup_and_unregister_workflow(client):
    """Test complete workflow: signup, verify, unregister, verify"""
    # Arrange
    email = "workflowtest@mergington.edu"
    activity_name = "Programming Class"
    
    # Act & Assert - Signup
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    assert signup_response.status_code == 200
    assert email in activities[activity_name]["participants"]
    
    # Act & Assert - Verify in GET
    get_response = client.get("/activities")
    assert email in get_response.json()[activity_name]["participants"]
    
    # Act & Assert - Unregister
    unregister_response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    assert unregister_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    
    # Act & Assert - Verify removed in GET
    final_get_response = client.get("/activities")
    assert email not in final_get_response.json()[activity_name]["participants"]


def test_multiple_signups_different_activities(client):
    """Test that a student can sign up for multiple different activities"""
    # Arrange
    email = "multisignup@mergington.edu"
    
    # Act
    response1 = client.post("/activities/Chess Club/signup", params={"email": email})
    response2 = client.post("/activities/Programming Class/signup", params={"email": email})
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert email in activities["Chess Club"]["participants"]
    assert email in activities["Programming Class"]["participants"]


# ============================================================================
# Edge Case Tests
# ============================================================================

def test_empty_email(client):
    """Test signup with empty email parameter"""
    # Arrange
    activity_name = "Chess Club"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": ""}
    )
    
    # Assert
    # Should still process but with empty string - depends on validation
    assert response.status_code in [200, 400]


def test_special_characters_in_email(client):
    """Test signup with special characters in email"""
    # Arrange
    email = "test+tag@mergington.edu"
    activity_name = "Chess Club"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Assert
    assert response.status_code == 200
    assert email in activities[activity_name]["participants"]


# ============================================================================
# Performance/Load Tests (Optional)
# ============================================================================

def test_many_signups(client):
    """Test multiple signups to verify list handling"""
    # Arrange
    activity_name = "Programming Class"
    emails = [f"student{i}@mergington.edu" for i in range(10)]
    
    # Act
    for email in emails:
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        assert response.status_code == 200
    
    # Assert
    for email in emails:
        assert email in activities[activity_name]["participants"]
    
    assert len(activities[activity_name]["participants"]) >= len(emails) + 2  # +2 for initial participants
