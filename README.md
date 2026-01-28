📄 AI Resume Analyzer & Job Match System

An AI-powered web application that analyzes resumes against job descriptions, calculates skill match percentage, provides improvement suggestions, and allows users to export the analysis report as a PDF.

🚀 Features

📤 Upload Resume (PDF)

📝 Paste Job Description

🤖 AI-based Resume Analysis

📊 Skill Match Percentage with Progress Bar

👁 Resume Preview

💡 Skill & Improvement Suggestions

⏳ Progress Loader Animation during analysis

📄 Download Resume Analysis Report as PDF

🗄 MySQL Database Integration

🌐 Modern React UI

🧱 Tech Stack
Frontend

React.js

HTML5 / CSS3

JavaScript (ES6)

jsPDF & html2canvas (PDF Export)

Backend

Python

FastAPI

Uvicorn

Database

MySQL

MySQL Workbench

📁 Project Structure
Backend (ai-resume-analyzer)
src/
 ├─ api/
 │   ├─ routes.py
 │   └─ schemas.py
 ├─ ml/
 │   ├─ matcher.py
 │   ├─ extractor.py
 │   └─ preprocessor.py
 ├─ utils/
 │   └─ pdf_parser.py
 ├─ core/
 │   └─ database.py
 ├─ main.py
data/
 └─ skills_list.txt

Frontend (resume-analyzer-ui)
src/
 ├─ components/
 │   ├─ AnalyzerForm.jsx
 │   ├─ ResumePreview.jsx
 │   ├─ ResultModal.jsx
 │   └─ ProgressBar.jsx
 ├─ services/
 │   └─ api.js
 ├─ App.jsx
 ├─ index.js
 └─ styles.css

🖥️ Frontend Setup (React)
Step 1: Navigate to UI folder
cd resume-analyzer-ui

Step 2: Install dependencies
npm install

Step 3: Start React app
npm start


Frontend will run at:

http://localhost:3000

⚙️ Backend Setup (FastAPI)
Step 1: Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

Step 2: Install backend dependencies
pip install -r requirements.txt

Step 3: Start FastAPI server
uvicorn main:app --reload


Backend will run at:

http://localhost:8000

🗄️ Database Setup (MySQL)
Step 1: Create Database
CREATE DATABASE resume_analyzer;

Step 2: Use Database
USE resume_analyzer;

Step 3: (Optional) Create Tables
CREATE TABLE resume_analysis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    resume_name VARCHAR(255),
    match_percentage INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


MySQL is managed using MySQL Workbench

📥 API Endpoint
Analyze Resume
POST /api/analyze


Request:

file: Resume PDF

job_description: Text

Response:

{
  "match_score": 39.54,
  "missing_skills": ["Kubernetes", "Machine Learning"],
  "suggestions": [
    "Consider adding skills: Kubernetes, Machine Learning."
  ]
}


📄 PDF Export Feature

The resume analysis report can be downloaded as a real PDF using:

jsPDF

html2canvas

The PDF includes:

Match percentage

Skills analysis

Suggestions

Resume summary

📌 Important Notes

Ensure backend (localhost:8000) is running before submitting resume

Only PDF resumes are supported

CORS must be enabled in FastAPI for frontend communication

Internet connection is not required (local analysis)

🛠 Future Enhancements

User authentication (Login/Register)

Resume history dashboard

Multiple job comparison

AI model integration (OpenAI / HuggingFace)

Cloud deployment (AWS / Render)

🤝 Contributing

Contributions are welcome!

Fork the repository

Create your feature branch

Commit changes

Push to your branch

Create a Pull Request


👨‍💻 Author

Arijit Ghosh
Backend Developer | Java | Python | Spring Boot
📍 India
