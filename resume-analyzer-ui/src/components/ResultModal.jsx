import ProgressBar from "./ProgressBar";

export default function ResultModal({ result, onClose }) {
  return (
    <div className="modal-bg">
      <div className="modal">
        <span className="close" onClick={onClose}>×</span>

        <h2>Analysis Result</h2>

        <p><strong>Match Score:</strong> {result.match_score}%</p>
        <ProgressBar value={result.match_score} />

        <h3>Missing Skills</h3>
        <div>
          {result.missing_skills.map(skill => (
            <span className="chip" key={skill}>{skill}</span>
          ))}
        </div>

        <h3>Suggestions</h3>
        <ul>
          {result.suggestions.map((s, i) => <li key={i}>{s}</li>)}
        </ul>

        <button className="primary-btn" onClick={() => window.print()}>
          Download Report (PDF)
        </button>
      </div>
    </div>
  );
}
