from flask import json

from app import app


def test_riskOfStudentFailure():
    client = app.test_client()
    response = client.get('riskofstudentfailure/?cutoff=22&lecture=33&lab=22&support_sessions=44&canvas_activities=3')
    assert response.status_code == 200
    expected_result = {"risk_of_student_failure": "Student is not at risk"}
    assert json.loads(response.data) == expected_result


def test_totalAttendance():
    client = app.test_client()
    response = client.get('totalattendance/?att1=2&att2=3&att3=5&att4=7')
    assert response.status_code == 200
    expected_result = {"total_attendance": 17}
    assert json.loads(response.data) == expected_result


def test_sort():
    client = app.test_client()
    response = client.get(
        'sort/?item_1=Lecture%20sessions&attendance_1=4&item_2=Lab%20sessions&attendance_2=3&item_3=Support%20sessions'
        '&attendance_3=2&item_4=Canvas%20activities&attendance_4=2')
    assert response.status_code == 200
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
    assert json.loads(response.data) == expected_result


def test_minMax():
    client = app.test_client()
    response = client.get('maxmin/?item_1=Lecture%20sessions&attendance_1=4&item_2=Lab%20sessions&attendance_2=3&item_3'
                          '=Support%20sessions&attendance_3=2&item_4=Canvas%20activities&attendance_4=2')
    assert response.status_code == 200
    expected_result = {'attendance': ['4', '3', '2', '2'],
                       'error': False,
                       'items': ['Lecture sessions',
                                 'Lab sessions',
                                 'Support sessions',
                                 'Canvas activities'],
                       'max_item': 'Lecture sessions - 4',
                       'min_item': 'Canvas activities - 2'}
    assert json.loads(response.data) == expected_result


def test_studentEngagement():
    client = app.test_client()
    response = client.get('studentengagement/?lecture=90&lab=85&support_sessions=78&canvas_activities=92')
    print(response.data)
    print(response.content_type)
    assert response.status_code == 200
    expected_result = {"total_engagement": 2.880454545454546}
    assert json.loads(response.data) == expected_result


def test_averageAttendance():
    client = app.test_client()
    response = client.get('averageattendance/?lecture=90&lab=85&support_sessions=78&canvas_activities=92')
    assert response.status_code == 200
    expected_result = {'average': 86.25}
    assert json.loads(response.data) == expected_result


def test_invalidPath():
    client = app.test_client()
    response = client.get('/invalid_path')

    assert response.status_code == 404
