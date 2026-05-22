"""
scorer.py

Advanced ATS-style scoring system for resume evaluation.
"""


def calculate_skill_score(candidate_skills,
                          required_skills,
                          preferred_skills=None,
                          certifications=0):
    """
    Calculates skill score based on:
    - Required skill coverage
    - Preferred skill coverage
    - Certification bonus
    """

    if preferred_skills is None:
        preferred_skills = []

    # Required skill matching
    matched_required = 0

    for skill in required_skills:
        if skill.lower() in [candidate.lower() for candidate in candidate_skills]:
            matched_required += 1

    required_coverage = (
        matched_required / len(required_skills)
    ) * 100 if required_skills else 0

    # Preferred skill matching
    matched_preferred = 0

    for skill in preferred_skills:
        if skill.lower() in [candidate.lower() for candidate in candidate_skills]:
            matched_preferred += 1

    preferred_coverage = (
        matched_preferred / len(preferred_skills)
    ) * 100 if preferred_skills else 0

    # Weighted score
    skill_score = (
        required_coverage * 0.70
        + preferred_coverage * 0.30
    )

    # Certification bonus
    bonus = min(certifications * 2, 5)

    final_skill_score = min(skill_score + bonus, 100)

    return round(final_skill_score, 2)


def calculate_experience_score(candidate_experience,
                               required_experience):
    """
    Calculates experience score using ratio-based evaluation.
    """

    if required_experience == 0:
        return 100

    experience_ratio = candidate_experience / required_experience

    # Overqualification awareness
    capped_ratio = min(experience_ratio, 1.2)

    experience_score = capped_ratio * 100

    return round(min(experience_score, 100), 2)


def calculate_education_score(candidate_education,
                              required_education):
    """
    Calculates education score based on education level comparison.
    """

    education_levels = {
        "Diploma": 1,
        "Bachelors": 2,
        "Masters": 3,
        "PhD": 4
    }

    candidate_level = education_levels.get(candidate_education, 0)

    required_level = education_levels.get(required_education, 0)

    if candidate_level >= required_level:
        return 100

    elif candidate_level == required_level - 1:
        return 70

    elif candidate_level == required_level - 2:
        return 40

    return 10


def calculate_overall_score(skill_score,
                            experience_score,
                            education_score):
    """
    Calculates overall ATS score using weighted composite formula.
    """

    overall_score = (
        (skill_score * 0.55)
        + (experience_score * 0.30)
        + (education_score * 0.15)
    )

    return round(overall_score, 2)