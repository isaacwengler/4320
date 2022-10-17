import pytest
import System
from Student import Student

# Test that a student can submit an assignment
def test_submit_assignment(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(username, password)
    user = grading_system.usr
    assert type(user) == Student
    assert user.name == username

    course = 'cloud_computing'
    assignment_name = 'assignment1'
    submission = "code submission yeahhh"
    date = "10/11/22"
    user.submit_assignment(course, assignment_name, submission, date)

    grading_system.reload_data()
    database_assignment = user.courses[course][assignment_name]
    assert database_assignment['submission'] == submission
    assert database_assignment['submission_date'] == date

# Test that the check_ontime function returns the correct response
def test_check_ontime():
    due_date = '10/10/22'

    # do not need to instantiate a student since this is a util method.
    # the code should be changed to not require "self"
    test = Student.check_ontime(None, '10/5/22', due_date)
    assert test

    test2 = Student.check_ontime(None, '10/12/22', due_date)
    assert not test2

# Test that check_grades gives a student grades for a course
def test_check_grades(grading_system):
    username = 'yted91'
    password = 'imoutofpasswordnames'
    grading_system.login(username, password)
    user = grading_system.usr
    
    grades = user.check_grades('cloud_computing')
    assert grades == [['assignment1', 3], ['assignment2', 5]]

# Test that view_assignments gives a student assignments and due dates
def test_view_assignments(grading_system):
    username = 'yted91'
    password = 'imoutofpasswordnames'
    grading_system.login(username, password)
    user = grading_system.usr
    
    assignments = user.view_assignments('software_engineering')
    assert assignments == [['assignment1', '1/1/20'], ['assignment2', '2/1/20']]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
