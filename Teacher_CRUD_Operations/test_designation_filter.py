import pytest
import requests
import random


def test_designation_filter(login_data, get_header):
    base_url, login_payload = login_data
    headers = get_header

    # Pick a random designation to filter by
    key_designation = random.choice(["Professor", "Associate Professor", "Assistant Professor", "Lecturer", "Instructor"])

    # Send GET request with designation filter
    response = requests.get(f'{base_url}/api/teacher?designation={key_designation}', headers=headers)
    teacher_list = response.json()

    # Validate response status code
    assert response.status_code == 200, \
        f"Get call failed. Response code: {response.status_code}"

    # Validate every teacher in the result has the searched designation
    for teacher in teacher_list:
        assert key_designation.lower() in teacher['designation'].lower(), \
            f"Teacher with designation '{teacher['designation']}' found, but searched for '{key_designation}'"

    print("Designation filter worked correctly.")
