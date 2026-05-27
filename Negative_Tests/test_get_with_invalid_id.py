import pytest
import requests 

def test_get_teacher_with_wrong_id(login_data, get_header):
    base_url, login_payload = login_data
    headers = get_header
    invalid_id = -152

    response = requests.get(f'{base_url}/api/teacher/{invalid_id}', headers=headers)
    

    #Status code is 404 validation
    assert response.status_code == 404, \
        f'Expected status code: 404, but found: {response.status_code}'
    
