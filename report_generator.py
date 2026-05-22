import json


def generate_report(candidate_data,
                    matched_skills,
                    missing_skills,
                    score,
                    recommendation):
    """
    Generates candidate analysis report.
    """

    report = {

        "candidate_email": candidate_data["email"],

        "skills_detected": candidate_data["skills"],

        "experience": candidate_data["experience"],

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "match_score": score,

        "recommendation": recommendation
    }

    return report


def save_report(report_data, output_path):
    """
    Saves report as JSON file.
    """

    with open(output_path, "w") as json_file:

        json.dump(report_data, json_file, indent=4)

    print("Report saved successfully.")