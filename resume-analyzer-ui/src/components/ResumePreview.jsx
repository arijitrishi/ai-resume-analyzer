export default function ResumePreview({ file }) {
  const url = URL.createObjectURL(file);

  return (
    <div className="resume-box">
      <iframe src={url} title="Resume Preview" />
    </div>
  );
}
