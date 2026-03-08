"""
Tests for signup endpoint (POST /activities/{activity_name}/signup)
Using Arrange-Act-Assert (AAA) pattern
"""


def test_signup_successful_adds_participant(client, fresh_activities, student_email):
    """
    Test successful signup adds participant to activity
    
    Arrange: Fresh activities and new student email prepared
    Act: POST request to signup endpoint with new student
    Assert: Returns 200, correct message, and participant is added to activity
    """
    # Arrange
    activity_name = "Chess Club"
    initial_count = len(fresh_activities[activity_name]["participants"])
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": student_email}
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {student_email} for {activity_name}"
    assert len(fresh_activities[activity_name]["participants"]) == initial_count + 1
    assert student_email in fresh_activities[activity_name]["participants"]


def test_signup_duplicate_returns_400(client, fresh_activities):
    """
    Test that duplicate signup attempt returns 400 error
    
    Arrange: Use existing participant from Chess Club
    Act: POST request to signup same participant again
    Assert: Returns 400 with "already signed up" error message
    """
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": existing_email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_signup_invalid_activity_returns_404(client, student_email):
    """
    Test that signup to non-existent activity returns 404
    
    Arrange: Use invalid activity name
    Act: POST request to non-existent activity
    Assert: Returns 404 with "Activity not found" error
    """
    # Arrange
    invalid_activity = "NonExistent Club"
    
    # Act
    response = client.post(
        f"/activities/{invalid_activity}/signup",
        params={"email": student_email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_increases_participant_count(client, fresh_activities, student_email):
    """
    Test that signup correctly updates participant count
    
    Arrange: Get initial participants count
    Act: POST signup request
    Assert: Participant count increases by exactly 1
    """
    # Arrange
    activity_name = "Programming Class"
    initial_count = len(fresh_activities[activity_name]["participants"])
    
    # Act
    client.post(
        f"/activities/{activity_name}/signup",
        params={"email": student_email}
    )
    
    # Assert
    final_count = len(fresh_activities[activity_name]["participants"])
    assert final_count == initial_count + 1
