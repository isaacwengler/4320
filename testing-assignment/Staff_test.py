import pytest
import System
from Staff import Staff


username = 'cmhbf5'
password = 'bestTA'


# Test that a staff member can change a student's grade
def test_change_grade(grading_system):
    student_user = 'hdjsr7'
    course = 'software_engineering'
    assignment = 'assignment1'
    new_grade = 75

    grading_system.login(username,password)
    user = grading_system.usr

    user.change_grade(student_user, course, assignment, new_grade)
    grading_system.reload_data()
    database_grade = user.users[student_user]['courses'][course][assignment]['grade']
    assert database_grade == new_grade

# Test that a staff member can create an assignment
def test_create_assignment(grading_system):
    course = 'software_engineering'
    assignment = 'new_assignment'
    due_date = '10/20/22'

    grading_system.login(username,password)
    user = grading_system.usr

    user.create_assignment(assignment, due_date, course)
    grading_system.reload_data()
    course_assignments = user.all_courses[course]['assignments']

    assert assignment in course_assignments

    database_due_date = course_assignments[assignment]['due_date']
    assert database_due_date == due_date

# Test that a staff member cannot change a students grade if they are not an instructor
def test_change_grade_not_allowed(grading_system):
    student_user = 'hdjsr7'
    course = 'databases'
    assignment = 'assignment1'
    new_grade = 75

    grading_system.login(username,password)
    user = grading_system.usr

    user.change_grade(student_user, course, assignment, new_grade)
    grading_system.reload_data()
    database_grade = user.users[student_user]['courses'][course][assignment]['grade']
    # 100 is the previous value
    assert database_grade == 100

# Test that a staff member cannot create an assignment if they are not an intructor
def test_create_assignment_not_allowed(grading_system):
    course = 'databases'
    assignment = 'nonexisitentAssignment'
    due_date = '10/20/22'

    grading_system.login(username,password)
    user = grading_system.usr

    user.create_assignment(assignment, due_date, course)
    grading_system.reload_data()
    course_assignments = user.all_courses[course]['assignments']

    assert assignment not in course_assignments

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
