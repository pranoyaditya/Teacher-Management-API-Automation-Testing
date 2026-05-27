import pytest
import requests


def test_access_teachers_without_token(login_data):
    base_url, login_payload = login_data

    expected_error_message = "Missing or invalid Authorization header"

    # Send GET request without any Authorization header
    response = requests.get(f'{base_url}/api/teacher')
    response_error_message = response.json().get('message')

    # Validate status code is 401
    assert response.status_code == 401, \
        f"Expected 401, but got: {response.status_code}"

    # Validate response body contains the correct error message
    assert response_error_message == expected_error_message, \
        f"Expected: '{expected_error_message}', but found: '{response_error_message}'"