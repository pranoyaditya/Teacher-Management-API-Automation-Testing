import pytest
import requests
from utils.helper_functions import create_teacher, update_teacher_data, delete_teacher


def test_every_field_update_reflection_in_response(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    new_teacher_object = new_teacher_data
    headers = get_header

    # Create a new teacher to run update tests on
    create_teacher_response = create_teacher(base_url, new_teacher_object, headers)
    assert create_teacher_response.status_code in [200, 201], \
        f"Teacher creation failed during test setup. Status: {create_teacher_response.status_code}"

    teacher = create_teacher_response.json()
    teacher_id = teacher['teacherId']

    # ── Name update ──────────────────────────────────────────────────────
    updated_teacher = update_teacher_data(teacher, name=True)
    name_update_response = requests.put(
        f'{base_url}/api/teacher/{teacher_id}',
        json=updated_teacher,
        headers=headers
    )
    response_data = name_update_response.json()

    assert name_update_response.status_code == 200, \
        f"Name update failed. Status code: {name_update_response.status_code}"
    assert response_data['name'] == updated_teacher['name'], \
        f"Updated name: '{updated_teacher['name']}' but response shows: '{response_data['name']}'"

    print("Name update was successful.")

    # ── Email update ─────────────────────────────────────────────────────
    updated_teacher = update_teacher_data(teacher, email=True)
    email_update_response = requests.put(
        f'{base_url}/api/teacher/{teacher_id}',
        json=updated_teacher,
        headers=headers
    )
    response_data = email_update_response.json()

    assert email_update_response.status_code == 200, \
        f"Email update failed. Status code: {email_update_response.status_code}"
    assert response_data['email'] == updated_teacher['email'], \
        f"Updated email: '{updated_teacher['email']}' but response shows: '{response_data['email']}'"

    print("Email update was successful.")

    # ── Department update ────────────────────────────────────────────────
    updated_teacher = update_teacher_data(teacher, department=True)
    department_update_response = requests.put(
        f'{base_url}/api/teacher/{teacher_id}',
        json=updated_teacher,
        headers=headers
    )
    response_data = department_update_response.json()

    assert department_update_response.status_code == 200, \
        f"Department update failed. Status code: {department_update_response.status_code}"
    assert response_data['department'] == updated_teacher['department'], \
        f"Updated department: '{updated_teacher['department']}' but response shows: '{response_data['department']}'"

    print("Department update was successful.")

    # ── Designation update ───────────────────────────────────────────────
    updated_teacher = update_teacher_data(teacher, designation=True)
    designation_update_response = requests.put(
        f'{base_url}/api/teacher/{teacher_id}',
        json=updated_teacher,
        headers=headers
    )
    response_data = designation_update_response.json()

    assert designation_update_response.status_code == 200, \
        f"Designation update failed. Status code: {designation_update_response.status_code}"
    assert response_data['designation'] == updated_teacher['designation'], \
        f"Updated designation: '{updated_teacher['designation']}' but response shows: '{response_data['designation']}'"

    print("Designation update was successful.")

    # Cleanup: delete the teacher created for this test
    delete_teacher(base_url, teacher_id, headers)
    print(f"Cleanup: teacher {teacher_id} deleted after test.")
