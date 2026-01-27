import spacy
from typing import List

nlp = spacy.load("en_core_web_sm")  # Load spaCy model

def preprocess_text(text: str) -> List[str]:
    """
    Preprocess text: tokenize, remove stopwords, lemmatize.
    Returns a list of cleaned tokens.
    """
    if not text:
        return []
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    return tokens