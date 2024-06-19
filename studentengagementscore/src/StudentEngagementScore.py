def student_engagement_calc(lture, lb, supp, canv):
    lecture = (lture * 0.3) / 33
    lab = (lb * 0.4) / 22
    support_sessions = (supp * 0.15) / 44
    canvas_activities = (canv * 0.15) / 55

    total = lecture + lab + support_sessions + canvas_activities
    return total
