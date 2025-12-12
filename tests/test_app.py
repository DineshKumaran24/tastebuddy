import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import app

from app import app

def test_home_redirect():
    response = app.test_client().get("/")
    assert response.status_code == 302

def test_login_page_loads():
    response = app.test_client().get("/login")
    assert response.status_code == 200

def test_feed_page_loads():
    response = app.test_client().get("/feed")
    assert response.status_code == 200

