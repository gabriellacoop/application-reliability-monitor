
import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_health_check_healthy(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_health_check_returns_json(client):
    response = client.get("/health")

    assert response.is_json
    assert "timestamp" in response.json


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == (
        "Application Reliability Monitor is running!"
    )
def test_metrics_endpoint(client):
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"app_health_checks_total" in response.data
    assert b"app_health_status" in response.data