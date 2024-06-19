from flask import json
from app import app
import time


def measure_time(func):
    def wrapper(*a, **b):
        start_time = time.time()
        result = func(*a, **b)
        end_time = time.time()
        print(f"{func.__name__} total time elapsed: {end_time - start_time} seconds")
        return result

    return wrapper


@measure_time
def test_riskOfStudentFailure():
    client = app.test_client()
    response = client.get('riskofstudentfailure/?cutoff=22&lecture=33&lab=22&support_sessions=44&canvas_activities=3')
    if response.status_code == 200:
        print("Risk Of Student Failure Service OK")
    else:
        print("Test failed with status code: ")
        print(response.status_code)
    expected_result = {"risk_of_student_failure": "Student is not at risk"}
    if json.loads(response.data) != expected_result:
        print("Expected result not returned from host")


@measure_time
def test_totalAttendance():
    client = app.test_client()
    response = client.get('totalattendance/?att1=2&att2=3&att3=5&att4=7')
    if response.status_code == 200:
        print("Total Student Attendance Service OK")
    else:
        print("Test failed with status code: ")
        print(response.status_code)
    expected_result = {"total_attendance": 17}
    if json.loads(response.data) != expected_result:
        print("Expected result not returned from host")


@measure_time
def test_sort():
    client = app.test_client()
    response = client.get(
        'sort/?item_1=Lecture%20sessions&attendance_1=4&item_2=Lab%20sessions&attendance_2=3&item_3=Support%20sessions'
        '&attendance_3=2&item_4=Canvas%20activities&attendance_4=2')
    if response.status_code == 200:
        print("Sort Service OK")
    else:
        print("Test failed with status code: ")
        print(response.status_code)
    expected_result = {'attendance': ['4', '3', '2', '2'],
                       'error': False,
                       'items': ['Lecture sessions',
                                 'Lab sessions',
                                 'Support sessions',
                                 'Canvas activities'],
                       'max_item': '',
                       'min_item': '',
                       'sorted_attendance': [{'attendance': '4', 'item': 'Lecture sessions'},
                                             {'attendance': '3', 'item': 'Lab sessions'},
                                             {'attendance': '2', 'item': 'Support sessions'},
                                             {'attendance': '2', 'item': 'Canvas activities'}]}
    if json.loads(response.data) != expected_result:
        print("Expected result not returned from host")


@measure_time
def test_minMax():
    client = app.test_client()
    response = client.get('maxmin/?item_1=Lecture%20sessions&attendance_1=4&item_2=Lab%20sessions&attendance_2=3&item_3'
                          '=Support%20sessions&attendance_3=2&item_4=Canvas%20activities&attendance_4=2')
    if response.status_code == 200:
        print("MinMax Service OK")
    else:
        print("Test failed with status code: ")
        print(response.status_code)

    expected_result = {'attendance': ['4', '3', '2', '2'],
                       'error': False,
                       'items': ['Lecture sessions',
                                 'Lab sessions',
                                 'Support sessions',
                                 'Canvas activities'],
                       'max_item': 'Lecture sessions - 4',
                       'min_item': 'Canvas activities - 2'}
    if json.loads(response.data) != expected_result:
        print("Expected result not returned from host")


@measure_time
def test_studentEngagement():
    client = app.test_client()
    response = client.get('studentengagement/?lecture=90&lab=85&support_sessions=78&canvas_activities=92')
    if response.status_code == 200:
        print("Student Engagement Service OK")
    else:
        print("Test failed with status code: ")
        print(response.status_code)
    expected_result = {"total_engagement": 2.880454545454546}
    if json.loads(response.data) != expected_result:
        print("Expected result not returned from host")


@measure_time
def test_averageAttendance():
    client = app.test_client()
    response = client.get('averageattendance/?lecture=90&lab=85&support_sessions=78&canvas_activities=92')
    if response.status_code == 200:
        print("Average Student Attendance Service OK")
    else:
        print("Test failed with status code: ")
        print(response.status_code)

    expected_result = {'average': 86.25}
    if json.loads(response.data) != expected_result:
        print("Expected result not returned from host")
