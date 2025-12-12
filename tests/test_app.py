import pytest
from app import app

# ----------------------------
# Fixture: create test client
# ----------------------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ----------------------------
# Test: Login page loads
# ----------------------------
def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data  # Checks that page contains "Login" text

# ----------------------------
# Test: Feed page requires login (redirect if not logged in)
# ----------------------------
def test_feed_requires_login(client):
    response = client.get("/feed")
    # Feed page should redirect (302) if not logged in
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]

# ----------------------------
# Test: Feed page loads after login
# ----------------------------
def test_feed_page_loads(client):
    # Simulate login
    with client.session_transaction() as session:
        session['logged_in'] = True
    
    response = client.get("/feed")
    assert response.status_code == 200
    assert b"Feed" in response.data  # Checks that page contains "Feed" text

# ----------------------------
# Test: Submitting feedback
# ----------------------------
def test_feedback_submission(client):
    # Simulate login
    with client.session_transaction() as session:
        session['logged_in'] = True

    feedback_data = {
        "feedback": "Great app!"
    }

    response = client.post("/feed", data=feedback_data)
    # Assuming your app redirects after posting feedback
    assert response.status_code in [200, 302]
