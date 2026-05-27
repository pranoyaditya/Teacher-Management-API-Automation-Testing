import pytest
import requests
import random


def test_department_filter(login_data, get_header):
    base_url, login_payload = login_data
    headers = get_header

    # Pick a random department to filter by
    key_department = random.choice(["CSE", "BBA", "MBA", "LAW", "PHARMACY", "ENGLISH"])

    # Send GET request with department filter
    response = requests.get(f'{base_url}/api/teacher?department={key_department}', headers=headers)
    teacher_list = response.json()

    # Validate response status code
    assert response.status_code == 200, \
        f"Get call failed. Response code: {response.status_code}"

    # Validate every teacher in the result belongs to the searched department
    for teacher in teacher_list:
        assert teacher['department'] == key_department, \
            f"Teacher from department '{teacher['department']}' found, but searched for '{key_department}'"

    print("Department filter worked correctly.")
