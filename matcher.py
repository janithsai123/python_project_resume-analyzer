def match_skills(candidate_skills, required_skills):
    """
    Matches candidate skills with required job skills.
    """

    matched_skills = []

    missing_skills = []

    for skill in required_skills:

        if skill.lower() in [candidate.lower() for candidate in candidate_skills]:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills