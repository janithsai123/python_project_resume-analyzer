from core.parser import parse_resume

from core.matcher import match_skills

from core.scorer import (
    calculate_skill_score,
    calculate_experience_score,
    calculate_education_score,
    calculate_overall_score
)

from core.recommender import generate_recommendation

from core.report_generator import generate_report, save_report


# Required job skills
JOB_REQUIRED_SKILLS = [
    "Python",
    "SQL",
    "Machine Learning"
]

# Preferred bonus skills
JOB_PREFERRED_SKILLS = [
    "Power BI",
    "Docker"
]

# Minimum required experience
REQUIRED_EXPERIENCE = 3

# Minimum education requirement
REQUIRED_EDUCATION = "Bachelors"


def main():

    # Resume file path
    resume_path = "data/resumes/sample_resume1.txt"

    # Parse resume data
    candidate_data = parse_resume(resume_path)

    # Match skills
    matched_skills, missing_skills = match_skills(
        candidate_data["skills"],
        JOB_REQUIRED_SKILLS
    )

    # Advanced skill score
    skill_score = calculate_skill_score(
        candidate_data["skills"],
        JOB_REQUIRED_SKILLS,
        JOB_PREFERRED_SKILLS,
        certifications=candidate_data["certifications"]
    )

    # Experience score
    experience_score = calculate_experience_score(
        candidate_data["experience"],
        REQUIRED_EXPERIENCE
    )

    # Education score
    education_score = calculate_education_score(
        candidate_data.get("education", "Bachelors"),
        REQUIRED_EDUCATION
    )

    # Final ATS score
    overall_score = calculate_overall_score(
        skill_score,
        experience_score,
        education_score
    )

    # Hiring recommendation
    recommendation = generate_recommendation(overall_score)

    # Generate report
    report = generate_report(
        candidate_data,
        matched_skills,
        missing_skills,
        overall_score,
        recommendation
    )

    # Save report as JSON
    save_report(
        report,
        "data/reports/candidate_report.json"
    )

    # Display analysis
    print("\n========== RESUME ANALYSIS ==========\n")

    print(f"Candidate Email: {candidate_data['email']}")

    print(f"\nDetected Skills: {candidate_data['skills']}")

    print(f"\nMatched Skills: {matched_skills}")

    print(f"\nMissing Skills: {missing_skills}")

    print(f"\nExperience: {candidate_data['experience']} years")

    print(f"\nSkill Score: {skill_score}%")

    print(f"Experience Score: {experience_score}%")

    print(f"Education Score: {education_score}%")

    print(f"\nOverall ATS Score: {overall_score}%")

    print(f"\nRecommendation: {recommendation}")

    print("\n====================================\n")


if __name__ == "__main__":
    main()