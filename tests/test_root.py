"""
Tests for root endpoint (GET /)
Using Arrange-Act-Assert (AAA) pattern
"""


def test_root_redirects_to_static(client):
    """
    Test that GET / redirects to /static/index.html
    
    Arrange: Client is ready (from fixture)
    Act: Make GET request to root
    Assert: Response status is 307 (redirect) and location header points to /static/index.html
    """
    # Arrange (implicit via client fixture)
    
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
