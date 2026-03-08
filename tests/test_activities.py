"""
Tests for activities endpoint (GET /activities)
Using Arrange-Act-Assert (AAA) pattern
"""


def test_get_activities_returns_all_activities(client, fresh_activities):
    """
    Test that GET /activities returns all activities
    
    Arrange: Fresh activities data is prepared
    Act: Make GET request to /activities
    Assert: Response contains all activities with correct count
    """
    # Arrange (implicit via fresh_activities fixture)
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    
    # Assert
    assert response.status_code == 200
    assert len(activities) == 3
    assert "Chess Club" in activities
    assert "Programming Class" in activities
    assert "Gym Class" in activities


def test_get_activities_returns_correct_structure(client, fresh_activities):
    """
    Test that each activity has correct structure and fields
    
    Arrange: Fresh activities data is prepared
    Act: Make GET request and extract first activity
    Assert: Activity has all required fields with correct types
    """
    # Arrange (implicit via fresh_activities fixture)
    
    # Act
    response = client.get("/activities")
    activities = response.json()
    chess_club = activities["Chess Club"]
    
    # Assert
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)
    assert len(chess_club["participants"]) == 2


def test_get_activities_returns_200_status(client, fresh_activities):
    """
    Test that GET /activities returns 200 status code
    
    Arrange: Fresh activities data prepared
    Act: Make GET request to /activities
    Assert: Response status code is 200
    """
    # Arrange (implicit via fresh_activities fixture)
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
