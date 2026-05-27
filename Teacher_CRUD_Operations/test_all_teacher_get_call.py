import pytest 

def test_get_all_teachers(login_data, teacher_data, schema_structure):
    base_url, login_payload = login_data 
    teachers, get_call_status_code = teacher_data 
    schema = schema_structure 

    # Validates response code is 200 
    assert get_call_status_code == 200, \
        f'Response status code is {get_call_status_code}'
    
    # Validate teachers array is not none 
    assert teachers is not None , f'Get call failed'

    # Validates the schema and data type of each teacher object 
    for teacher in teachers:
        for key, expected_type in schema.items():
            assert key in teacher, f'Key {key} is missing in teacher object'
            assert type(teacher[key]) == expected_type, \
                f'Invalid data type. Required {expected_type} : Got {type(teacher[key])}'
            
    # Final message 
    print('Get call for all teachers is successfull.')


    

