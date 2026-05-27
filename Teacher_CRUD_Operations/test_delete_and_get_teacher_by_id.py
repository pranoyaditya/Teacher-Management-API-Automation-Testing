import pytest
import requests
from utils.helper_functions import create_teacher


def test_delete_and_get_teacher_after_deletion(login_data, get_header, new_teacher_data):
    base_url, login_payload = login_data
    headers = get_header

    
    create_response = create_teacher(base_url, new_teacher_data, headers)
    assert create_response.status_code in [200, 201], \
        f"Teacher creation failed during test setup. Status: {create_response.status_code}"

    teacher_id = create_response.json()['teacherId']

    # Send DELETE request
    delete_response = requests.delete(f'{base_url}/api/teacher/{teacher_id}', headers=headers)

    # Validate response status code is 200 or 204
    assert delete_response.status_code in [200, 204], \
        f"Delete request was unsuccessful. Status code: {delete_response.status_code}"

    print("Delete request was successful.")

    # Send GET request for the deleted teacher
    get_response = requests.get(f'{base_url}/api/teacher/{teacher_id}', headers=headers)

    # Validate response status code is 404 — teacher should no longer exist
    assert get_response.status_code == 404, \
        f"Expected status code 404 after deletion, but got: {get_response.status_code}"

    print("After deletion, teacher was not found — as expected.")
