"""
skill_database.py

This file contains predefined technical and soft skills
used for resume analysis and candidate matching.
"""

SKILL_DATABASE = {

    "programming_languages": [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "TypeScript",
        "Go",
        "Ruby",
        "PHP"
    ],

    "database_skills": [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Oracle"
    ],

    "data_science_skills": [
        "Machine Learning",
        "Deep Learning",
        "Data Analysis",
        "Data Visualization",
        "Statistics",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow"
    ],

    "web_development": [
        "HTML",
        "CSS",
        "React",
        "Node.js",
        "Django",
        "Flask",
        "FastAPI"
    ],

    "tools_and_platforms": [
        "Git",
        "GitHub",
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "Power BI",
        "Excel"
    ],

    "soft_skills": [
        "Communication",
        "Leadership",
        "Problem Solving",
        "Teamwork",
        "Time Management"
    ]
}
ALL_SKILLS = []

for category in SKILL_DATABASE.values():
    ALL_SKILLS.extend(category)

EDUCATION_LEVELS = [
    "Diploma",
    "Bachelors",
    "Masters",
    "PhD"
]
            
