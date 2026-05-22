"""
recommender.py

Hiring recommendation engine based on ATS score.
"""


def generate_recommendation(score):
    """
    Generates recommendation based on overall ATS score.
    """

    if score >= 80:
        return "🟢 Strong Match — Recommended for Interview"

    elif score >= 65:
        return "🔵 Good Match — Consider for Interview"

    elif score >= 50:
        return "🟡 Partial Match — Review Manually"

    elif score >= 35:
        return "🟠 Weak Match — Not Recommended"

    return "🔴 Poor Match — Does Not Meet Requirements"