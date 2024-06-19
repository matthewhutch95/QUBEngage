import json
from app import app
import math
from StudentEngagementScore import student_engagement_calc


def test_app_request():
    client = app.test_client()
    response = client.get('/?lecture=10&lab=15&support_sessions=20&canvas_activities=25')
    assert response.status_code == 200
    expected_result = {'total_engagement': 0.5}
    assert json.loads(response.data) == expected_result


def test_valid_student_engagement_score():
    lt = 11
    lb = 22
    supp = 32
    canv = 43
    expected_result = (lt * 0.3) / 33 + (lb * 0.4) / 22 + (supp * 0.15) / 44 + (canv * 0.15) / 55
    result = student_engagement_calc(lt, lb, supp, canv)
    assert math.isclose(result, expected_result, rel_tol=1e-9)
