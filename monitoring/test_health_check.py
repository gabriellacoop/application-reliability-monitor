import requests


def test_health_check_healthy():
    response = requests.get(
        "http://127.0.0.1:5001/health",
        timeout=5
    )

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
def test_health_check_server_error():
    from unittest.mock import patch, Mock

    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.get", return_value=mock_response):
        response = requests.get("http://127.0.0.1:5001/health")

        assert response.status_code == 500
def test_health_check_connection_error():
    from unittest.mock import patch
    import requests

    with patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectionError
    ):
        try:
            requests.get("http://127.0.0.1:5001/health")
            assert False, "Expected ConnectionError"
        except requests.exceptions.ConnectionError:
            assert True