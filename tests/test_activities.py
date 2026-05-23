import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_happy_path_signup_and_unregister():
    # Signup: new user to existing activity
    resp = client.post("/activities/Basketball Team/signup", params={"email": "test1@example.com"})
    assert resp.status_code == 200
    assert "Signed up test1@example.com for Basketball Team" in resp.json()["message"]

    # Double signup triggers error
    resp = client.post("/activities/Basketball Team/signup", params={"email": "test1@example.com"})
    assert resp.status_code == 400
    assert "already signed up" in resp.json()["detail"]

    # Unregister works
    resp = client.delete("/activities/Basketball Team/signup", params={"email": "test1@example.com"})
    assert resp.status_code == 200
    assert "Unregistered test1@example.com from Basketball Team" in resp.json()["message"]

    # Unregister again triggers error
    resp = client.delete("/activities/Basketball Team/signup", params={"email": "test1@example.com"})
    assert resp.status_code == 404
    assert "not signed up" in resp.json()["detail"]
