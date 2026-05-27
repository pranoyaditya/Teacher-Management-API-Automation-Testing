import pytest
import requests
import random


def test_name_filter(login_data, get_header, teacher_data):
    base_url, login_payload = login_data
    teacher_list, status_code = teacher_data
    headers = get_header

    # Choose a random teacher name from the current teacher list
    key_name = random.choice(teacher_list)['name']

    # Send GET request with name filter
    response = requests.get(f'{base_url}/api/teacher?name={key_name}', headers=headers)
    filtered_list = response.json()

    # Validate response status code
    assert response.status_code == 200, \
        f"Get call failed. Response code: {response.status_code}"

    # Validate every result matches the searched name (case-insensitive)
    for teacher in filtered_list:
        assert teacher['name'].lower() == key_name.lower(), \
            f"Searched name: '{key_name}', but found: '{teacher['name']}'"

    print("Name filter worked correctly.")


def test_email_filter(login_data, get_header, teacher_data):
    base_url, login_payload = login_data
    teacher_list, status_code = teacher_data
    headers = get_header

    # Choose a random teacher email from the current teacher list
    key_email = random.choice(teacher_list)['email']

    # Send GET request with email filter
    response = requests.get(f'{base_url}/api/teacher?email={key_email}', headers=headers)
    teacher = response.json()[0]

    # Validate response status code
    assert response.status_code == 200, \
        f"Get call failed. Response code: {response.status_code}"

    # Validate the returned teacher has the searched email
    assert teacher['email'] == key_email, \
        f"Searched email: '{key_email}', but found: '{teacher['email']}'"

    print("Email filter worked correctly.")


def test_teacher_id_filter(login_data, get_header, teacher_data):
    base_url, login_payload = login_data
    teacher_list, status_code = teacher_data
    headers = get_header

    # Choose a random teacherId from the current teacher list
    key_teacher_id = random.choice(teacher_list)['teacherId']

    # Send GET request with teacherId filter
    response = requests.get(f'{base_url}/api/teacher?teacherId={key_teacher_id}', headers=headers)
    teacher = response.json()[0]

    # Validate response status code
    assert response.status_code == 200, \
        f"Get call failed. Response code: {response.status_code}"

    # Validate the returned teacher has the searched teacherId
    assert teacher['teacherId'] == key_teacher_id, \
        f"Searched teacherId: '{key_teacher_id}', but found: '{teacher['teacherId']}'"

    print("TeacherId filter worked correctly.")
