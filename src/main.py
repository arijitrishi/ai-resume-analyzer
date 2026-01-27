from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .api.routes import router
from .utils.logger import setup_logging

setup_logging()

app = FastAPI(
    title="AI Resume Analyzer & Job Match System",
    description="Upload a resume PDF and job description to get a match score and suggestions.",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(router, prefix="/api", tags=["Analysis"])

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")
