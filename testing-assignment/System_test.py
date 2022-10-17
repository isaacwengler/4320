import pytest
import System
from Student import Student


username = 'hdjsr7'
password = 'pass1234'

# Test that a user can login, the user is set, and updates add data to the correct user
def test_login(grading_system):
    grading_system.login(username,password)
    user = grading_system.usr
    assert type(user) == Student
    assert user.name == username

    course = 'software_engineering'
    assignment_name = 'assignment2'
    submission = "this is the new submission"
    date = "10/10/22"
    user.submit_assignment(course, assignment_name, submission, date)

    grading_system.reload_data()
    database_submission = user.courses[course][assignment_name]['submission']
    assert database_submission == submission

# Test that check_password returns true when correct, and false when incorrect
def test_check_password(grading_system):
    test = grading_system.check_password(username, password)
    assert test
    test2 = grading_system.check_password(username,'pass1234')
    assert test2
    test3 = grading_system.check_password(username,'#YEET')
    assert not test3
    test4 = grading_system.check_password(username, password.upper())
    assert not test4

# Test that check_password returns false when giving a non-existent username
def test_check_password_wrong_username(grading_system):
    test = grading_system.check_password('idwx3c', password)
    assert not test

# Test that login returns false when giving a non-existent username
def test_login_wrong_username(grading_system):
    test = grading_system.login('idwx3c', password)
    assert not test

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
