import pytest
from app import app

# ---------------------------
# Fixture for test client
# ---------------------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ---------------------------
# Test login page loads
# ---------------------------
def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data

# ---------------------------
# Test feed redirects if not logged in
# ---------------------------
def test_feed_requires_login(client):
    response = client.get("/feed")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]

# ---------------------------
# Test feed page loads when logged in
# ---------------------------
def test_feed_page_loads(client):
    # Simulate login
    with client.session_transaction() as session:
        session['logged_in'] = True

    response = client.get("/feed")
    assert response.status_code == 200
    assert b"Feed" in response.data

# ---------------------------
# Test feedback submission
# ---------------------------
def test_feedback_submission(client):
    with client.session_transaction() as session:
        session['logged_in'] = True

    feedback_data = {
        "feedback": "Great app!"
    }

    response = client.post("/feed", data=feedback_data)
    assert response.status_code == 200
    assert b"Feedback submitted!" in response.data
