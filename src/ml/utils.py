import os
from typing import List

def load_skills_list(filepath: str = "data/skills_list.txt") -> List[str]:
    """Load a predefined list of skills from a file for keyword matching."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Skills list file not found: {filepath}")
    with open(filepath, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]