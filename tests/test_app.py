import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_data(client):
    response = client.get("/api/data")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}
