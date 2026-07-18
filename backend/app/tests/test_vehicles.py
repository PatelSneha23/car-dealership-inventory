from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_vehicles():
    response = client.get("/vehicles")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0