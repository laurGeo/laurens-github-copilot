"""
Tests for unregister endpoint (DELETE /activities/{activity_name}/unregister)
Using Arrange-Act-Assert (AAA) pattern
"""


def test_unregister_successful_removes_participant(client, fresh_activities):
    """
    Test successful unregister removes participant from activity
    
    Arrange: Fresh activities with existing participants
    Act: DELETE request to unregister an existing participant
    Assert: Returns 200, message is correct, participant removed from activity
    """
    # Arrange
    activity_name = "Chess Club"
    email_to_remove = "michael@mergington.edu"
    initial_count = len(fresh_activities[activity_name]["participants"])
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email_to_remove}
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email_to_remove} from {activity_name}"
    assert len(fresh_activities[activity_name]["participants"]) == initial_count - 1
    assert email_to_remove not in fresh_activities[activity_name]["participants"]


def test_unregister_nonexistent_participant_returns_400(client, fresh_activities, student_email):
    """
    Test that unregistering non-existent participant returns 400
    
    Arrange: Use email not registered for activity
    Act: DELETE request for participant not in activity
    Assert: Returns 400 with "not registered" error
    """
    # Arrange
    activity_name = "Chess Club"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": student_email}
    )
    
    # Assert
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"].lower()


def test_unregister_invalid_activity_returns_404(client, student_email):
    """
    Test that unregister from non-existent activity returns 404
    
    Arrange: Use invalid activity name
    Act: DELETE request to non-existent activity
    Assert: Returns 404 with "Activity not found" error
    """
    # Arrange
    invalid_activity = "Nonexistent Club"
    
    # Act
    response = client.delete(
        f"/activities/{invalid_activity}/unregister",
        params={"email": student_email}
    )
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_unregister_decreases_participant_count(client, fresh_activities):
    """
    Test that unregister correctly updates participant count
    
    Arrange: Get initial participants count
    Act: DELETE unregister request
    Assert: Participant count decreases by exactly 1
    """
    # Arrange
    activity_name = "Programming Class"
    email_to_remove = "emma@mergington.edu"
    initial_count = len(fresh_activities[activity_name]["participants"])
    
    # Act
    client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email_to_remove}
    )
    
    # Assert
    final_count = len(fresh_activities[activity_name]["participants"])
    assert final_count == initial_count - 1
