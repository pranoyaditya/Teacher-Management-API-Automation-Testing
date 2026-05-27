import pytest
import requests


def test_login(login_data):
    base_url, login_payload = login_data

    response = requests.post(f'{base_url}/login', json=login_payload)

    # Validate status code is 200
    assert response.status_code == 200, \
        f"Login failed. Response: {response.status_code}"

    # Validate token is present and not None
    token = response.json().get("authToken")
    assert token is not None, "Auth token not found in response"
