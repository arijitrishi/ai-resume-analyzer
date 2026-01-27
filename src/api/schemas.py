from pydantic import BaseModel, Field
from typing import List, Dict

class AnalyzeRequest(BaseModel):
    job_description: str = Field(..., min_length=1, description="Job description text")

class AnalysisResponse(BaseModel):
    id: int
    match_score: float
    extracted_resume: Dict[str, List[str]]
    missing_skills: List[str]
    suggestions: List[str]
    created_at: str

class ErrorResponse(BaseModel):
    error: str
    details: str = None