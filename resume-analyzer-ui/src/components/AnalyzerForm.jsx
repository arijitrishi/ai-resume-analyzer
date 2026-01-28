import { useState } from "react";
import { analyzeResume } from "../services/api";
import ResumePreview from "./ResumePreview";

export default function AnalyzerForm({ onResult }) {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file || !jobDesc) return alert("Upload resume & job description");

    setLoading(true);
    try {
      const data = await analyzeResume(file, jobDesc);
      onResult(data);
    } catch (err) {
      alert("Analysis failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h1 className="title">AI Resume Analyzer</h1>

      <div className="field">
        <label>Upload Resume (PDF)</label>
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </div>

      {file && (
        <div className="preview-section">
          <ResumePreview file={file} />
        </div>
      )}

      <div className="field">
        <label>Job Description</label>
        <textarea
          rows="6"
          placeholder="Paste job description here..."
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
        />
      </div>

      <button className="primary-btn" onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>
    </div>
  );
}
