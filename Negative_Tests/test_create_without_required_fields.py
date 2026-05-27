import pytest
import requests
from utils.helper_functions import create_invalid_teacher_object


def test_create_teacher_without_name_field(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    headers = get_header

    # Remove 'name' from the payload
    teacher = create_invalid_teacher_object(new_teacher_data, name=True)

    response = requests.post(f'{base_url}/api/teacher', headers=headers, json=teacher)

    expected_error = "Name is required"
    response_error = response.json().get('error')

    # Validate status code is 400
    assert response.status_code == 400, \
        f"Expected 400, but got: {response.status_code}"

    # Validate error message is correct
    assert expected_error == response_error, \
        f"Expected: '{expected_error}', but got: '{response_error}'"

    print("Teacher creation without name field was rejected correctly.")


def test_create_teacher_without_email_field(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    headers = get_header

    # Remove 'email' from the payload
    teacher = create_invalid_teacher_object(new_teacher_data, email=True)

    response = requests.post(f'{base_url}/api/teacher', headers=headers, json=teacher)

    expected_error = "Email is required"
    response_error = response.json().get('error')

    # Validate status code is 400
    assert response.status_code == 400, \
        f"Expected 400, but got: {response.status_code}"

    # Validate error message is correct
    assert expected_error == response_error, \
        f"Expected: '{expected_error}', but got: '{response_error}'"

    print("Teacher creation without email field was rejected correctly.")


def test_create_teacher_without_department_field(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    headers = get_header

    # Remove 'department' from the payload
    teacher = create_invalid_teacher_object(new_teacher_data, department=True)

    response = requests.post(f'{base_url}/api/teacher', headers=headers, json=teacher)

    expected_error = "Department is required"
    response_error = response.json().get('error')

    # Validate status code is 400
    assert response.status_code == 400, \
        f"Expected 400, but got: {response.status_code}"

    # Validate error message is correct
    assert expected_error == response_error, \
        f"Expected: '{expected_error}', but got: '{response_error}'"

    print("Teacher creation without department field was rejected correctly.")


def test_create_teacher_without_designation_field(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    headers = get_header

    # Remove 'designation' from the payload
    teacher = create_invalid_teacher_object(new_teacher_data, designation=True)

    response = requests.post(f'{base_url}/api/teacher', headers=headers, json=teacher)

    expected_error = "Designation is required"
    response_error = response.json().get('error')

    # Validate status code is 400
    assert response.status_code == 400, \
        f"Expected 400, but got: {response.status_code}"

    # Validate error message is correct
    assert expected_error == response_error, \
        f"Expected: '{expected_error}', but got: '{response_error}'"

    print("Teacher creation without designation field was rejected correctly.")


def test_create_teacher_without_teacher_id_field(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    headers = get_header

    # Remove 'teacherId' from the payload
    teacher = create_invalid_teacher_object(new_teacher_data, teacherId=True)

    response = requests.post(f'{base_url}/api/teacher', headers=headers, json=teacher)

    expected_error = "Teacher ID is required"
    response_error = response.json().get('error')

    # Validate status code is 400
    assert response.status_code == 400, \
        f"Expected 400, but got: {response.status_code}"

    # Validate error message is correct
    assert expected_error == response_error, \
        f"Expected: '{expected_error}', but got: '{response_error}'"

    print("Teacher creation without teacherId field was rejected correctly.")
