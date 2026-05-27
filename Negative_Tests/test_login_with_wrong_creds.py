import pytest
import requests


def test_login_with_wrong_credentials(login_data):
    base_url, login_payload = login_data

    # Append extra characters to make the password intentionally wrong
    login_payload['password'] += '00'
    response = requests.post(f'{base_url}/login', json=login_payload)

    valid_message = "Invalid credentials"
    response_message = response.json().get('message')

    # Validate status code is 401
    assert response.status_code == 401, \
        f"Expected 401, but found: {response.status_code}"

    # Validate response body contains the correct error message
    assert response_message == valid_message, \
        f"Expected: '{valid_message}', but found: '{response_message}'"

    print(response.json())
