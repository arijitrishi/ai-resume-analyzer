import { useState } from "react";
import AnalyzerForm from "./components/AnalyzerForm";
import ResultModal from "./components/ResultModal";
import "./styles.css";

export default function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app-bg">
      <AnalyzerForm onResult={setResult} />
      {result && (
        <ResultModal result={result} onClose={() => setResult(null)} />
      )}
    </div>
  );
}
