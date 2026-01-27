from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Tuple
from .extractor import extract_resume_data
from .preprocessor import preprocess_text

def compute_match_score(resume_text: str, jd_text: str) -> float:
    """Compute match score (0-100%) using TF-IDF and cosine similarity."""
    if not resume_text or not jd_text:
        return 0.0
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(similarity * 100, 2)

def find_missing_skills(resume_skills: List[str], jd_text: str) -> List[str]:
    """
    Find skills in JD not present in resume.
    Handles case-insensitive matching and multi-word skills.
    """
    # Load skills list and normalize
    skills_list = [skill.lower() for skill in load_skills_list()]  # all known skills in lowercase
    resume_skills_lower = [s.lower() for s in resume_skills]

    # Preprocess JD
    jd_text_lower = jd_text.lower()

    # Find skills present in JD but missing in resume
    missing = []
    for skill in skills_list:
        if skill in jd_text_lower and skill not in resume_skills_lower:
            missing.append(skill)

    return missing



def generate_suggestions(missing_skills: List[str], resume_data: Dict[str, List[str]]) -> List[str]:
    suggestions = []
    if missing_skills:
        suggestions.append(f"Consider adding skills: {', '.join([s.title() for s in missing_skills])}.")
    if not resume_data["experience"]:
        suggestions.append("Highlight more work experience in your resume.")
    if not resume_data["education"]:
        suggestions.append("Include educational qualifications.")
    return suggestions


def analyze_resume_vs_job(resume_text: str, jd_text: str) -> Dict:
    """Full analysis: extract data, compute score, find gaps, suggest improvements."""
    resume_data = extract_resume_data(resume_text)
    score = compute_match_score(resume_text, jd_text)
    missing_skills = find_missing_skills(resume_data["skills"], jd_text)
    suggestions = generate_suggestions(missing_skills, resume_data)
    return {
        "match_score": score,
        "extracted_resume": resume_data,
        "missing_skills": missing_skills,
        "suggestions": suggestions,
    }
def load_skills_list(file_path="data/skills_list.txt") -> List[str]:
    """Load a list of known skills from a file."""
    try:
        with open(file_path, "r") as f:
            skills = [line.strip() for line in f if line.strip()]
        return skills
    except FileNotFoundError:
        raise FileNotFoundError(f"Skills list file not found: {file_path}")
    