import pytest
import System
from Staff import Staff


username = 'goggins'
password = 'augurrox'


# Test that a professor can add a student to a course
def test_add_student(grading_system):
    new_student = 'akend3'
    course = 'software_engineering'

    grading_system.login(username,password)
    user = grading_system.usr

    user.add_student(new_student, course)
    grading_system.reload_data()

    student = user.users[new_student]
    student_courses = student['courses']
    assert course in student_courses

# Test that a professor can drop a student to a course
def test_drop_student(grading_system):
    course = 'databases'
    student_to_drop = 'akend3'

    grading_system.login(username,password)
    user = grading_system.usr

    user.drop_student(student_to_drop, course)
   
    student = user.users[student_to_drop]
    student_courses = student['courses']
    assert course not in student_courses

# Test that a professor cannot drop a student to a course they do not instruct
def test_drop_student_not_allowed(grading_system):
    course = 'comp_sci'
    student_to_drop = 'akend3'

    grading_system.login(username,password)
    user = grading_system.usr

    user.drop_student(student_to_drop, course)
   
    student = user.users[student_to_drop]
    student_courses = student['courses']
    assert course in student_courses

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
