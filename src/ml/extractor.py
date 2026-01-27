import spacy
from typing import Dict, List
from .utils import load_skills_list
from .preprocessor import preprocess_text

nlp = spacy.load("en_core_web_sm")

def extract_skills(text: str) -> List[str]:
    """Extract skills using keyword matching + basic NLP (e.g., nouns)."""
    skills_list = load_skills_list()
    tokens = preprocess_text(text)
    extracted = []
    doc = nlp(text.lower())
    for token in doc:
        if token.lemma_ in skills_list and token.pos_ in ["NOUN", "PROPN"]:
            extracted.append(token.lemma_)
    return list(set(extracted))  # Remove duplicates

def extract_experience(text: str) -> List[str]:
    """Extract experience snippets (basic rule: sentences with years/roles)."""
    doc = nlp(text)
    experiences = []
    for sent in doc.sents:
        if any(word in sent.text.lower() for word in ["years", "experience", "worked", "role"]):
            experiences.append(sent.text.strip())
    return experiences[:5]  # Limit to top 5 for brevity

def extract_education(text: str) -> List[str]:
    """Extract education using NER (e.g., ORG entities like universities)."""
    doc = nlp(text)
    educations = [ent.text for ent in doc.ents if ent.label_ == "ORG" and any(word in ent.text.lower() for word in ["university", "college", "degree"])]
    return list(set(educations))

def extract_resume_data(text: str) -> Dict[str, List[str]]:
    """Extract all resume data: skills, experience, education."""
    return {
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "education": extract_education(text),
    }