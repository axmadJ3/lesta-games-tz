import pytest

from app import app 


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
