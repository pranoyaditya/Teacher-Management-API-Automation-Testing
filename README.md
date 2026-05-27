# Teacher-Management-API-Automation-Testing
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-orange)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Library-yellow)
![Allure](https://img.shields.io/badge/Allure-Test%20Report-brightgreen)
![HTML Report](https://img.shields.io/badge/HTML-Test%20Report-red)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black)

---

A simple API test automation project built with **Python** and **Pytest**, created as part of a QA Automation learning assignment.
The project automates the Teacher APIs of a Student Management System and covers authentication, CRUD operations, filter validations, and negative test scenarios.

---

## Project Structure

```
teacher-api-automation/
│
├── auth/
│   ├── __init__.py
│   └── test_login_api.py
│
├── teacher_crud_operations/
│   ├── __init__.py
│   ├── test_all_teacher_get_call.py
│   ├── test_new_teacher_creation.py
│   ├── test_update_teacher_fields.py
│   ├── test_delete_and_get_teacher_by_id.py
│   ├── test_department_filter.py
│   ├── test_designation_filter.py
│   └── test_name_teacherid_email_filter.py
│
├── negative_tests/
│   ├── __init__.py
│   ├── test_login_with_wrong_creds.py
│   ├── test_access_without_token.py
│   ├── test_get_with_invalid_id.py
│   └── test_create_without_required_fields.py
│
├── utils/
│   ├── __init__.py
│   └── helper_functions.py
│
├── reports/
│   ├── report.html       ← HTML report (auto-generated)
│   └── allure-results/   ← Allure raw results (auto-generated)
│   
├── conftest.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Tech Stack

- **Language:** Python 3.x
- **Test Framework:** Pytest
- **HTTP Library:** Requests
- **Fake Data:** Faker
- **Environment Variables:** python-dotenv
- **Reporting:** pytest-html, Allure Report

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/teacher-api-automation.git
cd teacher-api-automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Allure CLI (required to open the Allure report)

**Windows (via Scoop):**
```bash
scoop install allure
```

**Mac (via Homebrew):**
```bash
brew install allure
```

**Verify installation:**
```bash
allure --version
```

---

## How to Run Tests

Make sure your virtual environment is active and you are in the project root folder before running any command.

### Run all tests

```bash
pytest
```

### Run a specific folder

```bash
pytest auth/
pytest teacher_crud_operations/
pytest negative_tests/
```

### Run a specific file

```bash
pytest auth/test_login_api.py
```

### Run a specific test function

```bash
pytest auth/test_login_api.py::test_login
```

### Run with print() output visible

```bash
pytest -s
```

### Run with full verbose output

```bash
pytest -v -s
```

---

## Reporting

This project supports two types of reports.

---

### HTML Report

The HTML report is generated **automatically** after every test run. No extra command is needed — `pytest.ini` handles it.

The report is saved at:

```
reports/report.html
```

Just open that file in any browser after running `pytest`.

---

### Allure Report

Allure gives a more visual, detailed report with graphs and test history.

**Step 1 — Run tests and collect Allure results:**

```bash
pytest --alluredir=reports/allure-results
```

**Step 2 — Open the Allure report in your browser:**

```bash
allure serve reports/allure-results
```

This automatically opens the report in your default browser.

If you want to generate a static report folder instead:

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

---

## Test Cases

| # | Folder | File | Test | Type |
|---|--------|------|------|------|
| 1 | auth | test_login_api.py | Login returns 200 and token exists in response | Positive |
| 2 | teacher_crud_operations | test_all_teacher_get_call.py | Get all teachers — status code, schema, and data types | Positive |
| 3 | teacher_crud_operations | test_new_teacher_creation.py | Create teacher — status code and all fields match request | Positive |
| 4 | teacher_crud_operations | test_update_teacher_fields.py | Update name, email, department, and designation | Positive |
| 5 | teacher_crud_operations | test_delete_and_get_teacher_by_id.py | Delete teacher then GET by ID returns 404 | Positive |
| 6 | teacher_crud_operations | test_department_filter.py | Department filter returns only matching teachers | Positive |
| 7 | teacher_crud_operations | test_designation_filter.py | Designation filter returns only matching teachers | Positive |
| 8 | teacher_crud_operations | test_name_teacherid_email_filter.py | Name filter works correctly | Positive |
| 9 | teacher_crud_operations | test_name_teacherid_email_filter.py | Email filter works correctly | Positive |
| 10 | teacher_crud_operations | test_name_teacherid_email_filter.py | TeacherId filter works correctly | Positive |
| 11 | negative_tests | test_login_with_wrong_creds.py | Wrong credentials return 401 with correct error message | Negative |
| 12 | negative_tests | test_access_without_token.py | Request without token returns 401 with correct error message | Negative |
| 13 | negative_tests | test_get_with_invalid_id.py | GET with non-existent teacher ID returns 404 | Negative |
| 14 | negative_tests | test_create_without_required_fields.py | Create teacher without name returns 400 | Negative |
| 15 | negative_tests | test_create_without_required_fields.py | Create teacher without email returns 400 | Negative |
| 16 | negative_tests | test_create_without_required_fields.py | Create teacher without department returns 400 | Negative |
| 17 | negative_tests | test_create_without_required_fields.py | Create teacher without designation returns 400 | Negative |
| 18 | negative_tests | test_create_without_required_fields.py | Create teacher without teacherId returns 400 | Negative |

---

## API Reference

**Base URL:** `http://54.255.195.111:5171`

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /login | Login and get auth token |
| POST | /api/teacher | Create a new teacher |
| GET | /api/teacher | Get all teachers (supports filters) |
| GET | /api/teacher/{teacherId} | Get a single teacher by ID |
| PUT | /api/teacher/{teacherId} | Update a teacher |
| DELETE | /api/teacher/{teacherId} | Delete a teacher |

Full API docs: `http://54.255.195.111:5171/api-docs/#/`

---

## Screenshots and Video Recording

📁 [Google Drive Folder](https://drive.google.com/drive/folders/10qDbR4tE_s5nCHYf_L8wHFOwePBZGBgs?usp=sharing)

The Drive folder contains:
- HTML report screenshot
- Allure report screenshot

---

## Author
Preetom Aditya Pranoy
