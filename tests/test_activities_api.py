from copy import deepcopy

import pytest
from httpx import ASGITransport, AsyncClient

from src.app import activities, app


INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    snapshot = deepcopy(INITIAL_ACTIVITIES)
    activities.clear()
    activities.update(snapshot)


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.mark.anyio
async def test_signup_rejects_duplicate_participants(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    # Act
    first = await client.post(
        f"/activities/{activity_name}/signup", params={"email": email}
    )
    second = await client.post(
        f"/activities/{activity_name}/signup", params={"email": email}
    )

    # Assert
    assert first.status_code == 200
    assert second.status_code == 400
    assert second.json()["detail"] == "Student is already signed up"
    assert activities[activity_name]["participants"].count(email) == 1


@pytest.mark.anyio
async def test_unregister_removes_participant(client):
    # Arrange
    activity_name = "Programming Class"
    email = "to.remove@mergington.edu"
    await client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Act
    unregister = await client.delete(
        f"/activities/{activity_name}/signup", params={"email": email}
    )
    unregister_again = await client.delete(
        f"/activities/{activity_name}/signup", params={"email": email}
    )

    # Assert
    assert unregister.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert unregister_again.status_code == 404
