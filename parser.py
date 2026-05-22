import re
from utils.skill_database import (
    ALL_SKILLS,
    EDUCATION_LEVELS
)


def read_resume(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            resume_content = file.read()

        return resume_content

    except FileNotFoundError:
        print("Resume file not found.")
        return ""


def extract_email(resume_text):

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    found_emails = re.findall(email_pattern, resume_text)

    if found_emails:
        return found_emails[0]

    return "Email not found"

def extract_phone(resume_text):
    """
    Extracts phone number from resume text.
    """

    phone_pattern = r"\b\d{10}\b"

    found_numbers = re.findall(phone_pattern, resume_text)

    if found_numbers:
        return found_numbers[0]

    return "Phone number not found"

def extract_skills(resume_text):

    detected_skills = []

    resume_text = resume_text.lower()

    for skill in ALL_SKILLS:

        if skill.lower() in resume_text:
            detected_skills.append(skill)

    return detected_skills

def extract_experience(resume_text):
    """
    Extracts years of experience from resume text.
    """

    experience_pattern = r"(\d+)\s+years?"

    matched_experience = re.findall(experience_pattern, resume_text.lower())

    if matched_experience:
        return int(matched_experience[0])

    return 0

def extract_education(resume_text):
    """
    Extracts highest education level from resume.
    """

    for education in EDUCATION_LEVELS:

        if education.lower() in resume_text.lower():
            return education

    return "Not Mentioned"

def extract_certifications(resume_text):
    """
    Detects certifications mentioned in resume.
    """

    certification_keywords = [
        "certified",
        "certificate",
        "AWS Certified",
        "Google Certified",
        "Microsoft Certified"
    ]

    certification_count = 0

    for keyword in certification_keywords:

        if keyword.lower() in resume_text.lower():
            certification_count += 1

    return certification_count

def parse_resume(file_path):
    """
    Complete resume parsing function.
    """

    resume_text = read_resume(file_path)

    extracted_data = {

        "email": extract_email(resume_text),

        "phone": extract_phone(resume_text),

        "skills": extract_skills(resume_text),

        "experience": extract_experience(resume_text),

        "education": extract_education(resume_text),

        "certifications": extract_certifications(resume_text)
    }

    return extracted_data