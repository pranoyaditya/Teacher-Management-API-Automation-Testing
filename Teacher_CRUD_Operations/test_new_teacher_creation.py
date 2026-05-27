import pytest
import requests


def test_create_teacher(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    headers = get_header

    # Send POST request to create a new teacher
    response = requests.post(f'{base_url}/api/teacher', json=new_teacher_data, headers=headers)
    response_data = response.json()

    # Validate response status code
    assert response.status_code in [200, 201], \
        f"Teacher creation failed. Status code: {response.status_code}"

    # Validate name matches what was sent
    assert new_teacher_data['name'] == response_data['name'], \
        f"Response name: '{response_data['name']}' didn't match sent name: '{new_teacher_data['name']}'"

    # Validate email matches what was sent
    assert new_teacher_data['email'] == response_data['email'], \
        f"Response email: '{response_data['email']}' didn't match sent email: '{new_teacher_data['email']}'"

    # Validate department matches what was sent
    assert new_teacher_data['department'] == response_data['department'], \
        f"Response department: '{response_data['department']}' didn't match sent department: '{new_teacher_data['department']}'"

    # Validate teacherId matches what was sent
    assert new_teacher_data['teacherId'] == response_data['teacherId'], \
        f"Response teacherId: '{response_data['teacherId']}' didn't match sent teacherId: '{new_teacher_data['teacherId']}'"

    # Validate designation matches what was sent
    assert new_teacher_data['designation'] == response_data['designation'], \
        f"Response designation: '{response_data['designation']}' didn't match sent designation: '{new_teacher_data['designation']}'"

    print("Teacher created successfully.")
