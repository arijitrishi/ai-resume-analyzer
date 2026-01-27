from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db, Analysis
from ..ml.matcher import analyze_resume_vs_job
from ..utils.pdf_parser import extract_text_from_pdf
from .schemas import AnalysisResponse, ErrorResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post(
    "/analyze",
    response_model=AnalysisResponse,
    responses={400: {"model": ErrorResponse}}
)
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Analyze resume PDF against job description.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        resume_text = extract_text_from_pdf(await file.read())
        if not resume_text:
            raise HTTPException(status_code=400, detail="Could not extract text from PDF.")

        result = analyze_resume_vs_job(resume_text, job_description)

        db_analysis = Analysis(
            resume_text=resume_text,
            job_description=job_description,
            match_score=int(result["match_score"]),
            extracted_resume=result["extracted_resume"],
            missing_skills=result["missing_skills"],
            suggestions=result["suggestions"]
        )

        db.add(db_analysis)
        db.commit()
        db.refresh(db_analysis)

        return AnalysisResponse(
            id=db_analysis.id,
            match_score=result["match_score"],
            extracted_resume=result["extracted_resume"],
            missing_skills=result["missing_skills"],
            suggestions=result["suggestions"],
            created_at=db_analysis.created_at.isoformat()
        )

    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during analysis.")
