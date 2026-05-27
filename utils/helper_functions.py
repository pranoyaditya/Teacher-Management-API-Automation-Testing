import requests, random
from faker import Faker 

# Sends POST /api/teacher and returns the response
def create_teacher(base_url, teacher_payload, headers):
    response = requests.post(f'{base_url}/api/teacher', json=teacher_payload, headers=headers)
    return response


# Sends DELETE /api/teacher/{teacher_id} and returns the response
def delete_teacher(base_url, teacher_id, headers):
    response = requests.delete(f'{base_url}/api/teacher/{teacher_id}', headers=headers)
    return response


def create_invalid_teacher_object(teacher, name=False, email=False, department=False, designation=False, teacherId=False):
    """
    Returns a copy of the teacher dict with one required field removed.
    Used to test that the API correctly rejects incomplete payloads.
    """
    if name:
        return {
            "email": teacher['email'],
            "department": teacher['department'],
            "teacherId": teacher['teacherId'],
            "designation": teacher['designation']
        }
    elif email:
        return {
            "name": teacher['name'],
            "department": teacher['department'],
            "teacherId": teacher['teacherId'],
            "designation": teacher['designation']
        }
    elif department:
        return {
            "name": teacher['name'],
            "email": teacher['email'],
            "teacherId": teacher['teacherId'],
            "designation": teacher['designation']
        }
    elif designation:
        return {
            "name": teacher['name'],
            "department": teacher['department'],
            "teacherId": teacher['teacherId'],
            "email": teacher['email']
        }
    else:
        # Removes teacherId
        return {
            "name": teacher['name'],
            "department": teacher['department'],
            "email": teacher['email'],
            "designation": teacher['designation']
        }


def update_teacher_data(teacher_info, name=False, email=False, department=False, designation=False):
    """
    Returns an updated teacher payload with one or more fields changed to new values.
    Each while loop ensures the new value is actually different from the current one.
    
    """
    faker = Faker()

    updated_name = teacher_info['name']
    updated_email = teacher_info['email']
    updated_department = teacher_info['department']
    updated_designation = teacher_info['designation']

    if name:
        new_name = faker.name()
        while updated_name == new_name:
            new_name = faker.name()
        updated_name = new_name

    if email:
        new_email = faker.email()
        while updated_email == new_email:
            new_email = faker.email()
        updated_email = new_email

    if department:
        new_dept = random.choice(["CSE", "BBA", "MBA", "LAW", "PHARMACY", "ENGLISH"])
        while updated_department == new_dept:
            new_dept = random.choice(["CSE", "BBA", "MBA", "LAW", "PHARMACY", "ENGLISH"])
        updated_department = new_dept

    if designation:
        new_designation = random.choice(["Professor", "Associate Professor", "Assistant Professor", "Lecturer", "Instructor"])
        # FIX: was 'new_age = random.choice(...)' — wrong variable name caused infinite loop
        while updated_designation == new_designation:
            new_designation = random.choice(["Professor", "Associate Professor", "Assistant Professor", "Lecturer", "Instructor"])
        updated_designation = new_designation

    return {
        'name': updated_name,
        'email': updated_email,
        'department': updated_department,
        'designation': updated_designation
    }