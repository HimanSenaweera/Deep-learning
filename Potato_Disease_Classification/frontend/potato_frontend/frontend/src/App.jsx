import React, { useState } from "react";
import "./App.css";

function App() {
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    setPreview(URL.createObjectURL(file));
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="container">
      <div className="overlay">
        <div className="upload-box">
          <label htmlFor="file-input" className="drop-zone">
            <p>
              Drag and drop an image of a<br />
              potato plant leaf to process
            </p>
            <img src="/upload-icon.png" alt="upload" className="upload-icon" />
          </label>
          <input
            id="file-input"
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            hidden
          />

          {preview && (
            <div className="preview-section">
              <img src={preview} alt="preview" className="preview-image" />
              {result && (
                <p>
                  <strong>Class:</strong> {result.class} <br />
                </p>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
