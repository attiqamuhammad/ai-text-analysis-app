import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeText = async () => {
    if (!text.trim()) {
      setError("Please enter some text to analyze.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze-agent", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: text,
        }),
      });

      if (!response.ok) {
        throw new Error("Analysis failed.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(
        "Could not connect to the backend. Make sure your FastAPI server is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div className="brand">
          <div className="logo">
  <svg
    width="27"
    height="27"
    viewBox="0 0 32 32"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect
      x="5"
      y="4"
      width="18"
      height="24"
      rx="4"
      stroke="url(#logoGradient)"
      strokeWidth="2.5"
    />

    <path
      d="M10 11H18"
      stroke="url(#logoGradient)"
      strokeWidth="2.5"
      strokeLinecap="round"
    />

    <path
      d="M10 16H18"
      stroke="url(#logoGradient)"
      strokeWidth="2.5"
      strokeLinecap="round"
    />

    <circle
      cx="25"
      cy="8"
      r="3"
      fill="#06B6D4"
    />

    <path
      d="M25 5V11M22 8H28"
      stroke="#7C3AED"
      strokeWidth="1.5"
      strokeLinecap="round"
    />

    <defs>
      <linearGradient
        id="logoGradient"
        x1="5"
        y1="4"
        x2="25"
        y2="28"
        gradientUnits="userSpaceOnUse"
      >
        <stop stopColor="#2563EB" />
        <stop offset="0.5" stopColor="#06B6D4" />
        <stop offset="1" stopColor="#7C3AED" />
      </linearGradient>
    </defs>
  </svg>
</div>

          <div>
            <h1>AI Text Analysis</h1>
            <p>Understand your text with AI-powered analysis</p>
          </div>
        </div>
      </header>

      <main className="container">
        <section className="hero">
          <span className="badge">✦ AI CONTENT ANALYZER</span>

          <h2>Analyze your text</h2>

          <p>
            Get insights about sentiment, tone, safety, entities, key phrases,
            PII, topics, content type, and summary.
          </p>
        </section>

        <section className="input-card">
          <div className="input-header">
            <div>
              <h3>Your text</h3>
              <span>Enter any text you want to analyze</span>
            </div>

            <span className="counter">{text.length} characters</span>
          </div>

          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Example: I am very happy with my new job at Microsoft Corporation..."
          />

          {error && <div className="error">{error}</div>}

          <button
            className="analyze-button"
            onClick={analyzeText}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "✦ Analyze Text"}
          </button>
        </section>

        {result && (
          <section className="results">
            <div className="results-title">
              <h2>Analysis Results</h2>
              <span>9 insights generated</span>
            </div>

            <div className="result-grid">
              <div className="result-card">
                <div className="card-icon">😊</div>
                <h3>Sentiment</h3>
                <p>{result.sentiment?.sentiment}</p>
                <small>
                  Polarity: {result.sentiment?.polarity}
                </small>
              </div>

              <div className="result-card">
                <div className="card-icon">🎭</div>
                <h3>Tone</h3>
                <p>{result.tone?.tone}</p>
                <small>
                  Subjectivity: {result.tone?.subjectivity}
                </small>
              </div>

              <div className="result-card">
                <div className="card-icon">🛡️</div>
                <h3>Safety</h3>
                <p>{result.safety?.overall}</p>
              </div>

              <div className="result-card">
                <div className="card-icon">🏢</div>
                <h3>Named Entities</h3>

                {result.entities?.entities?.length ? (
                  result.entities.entities.map((entity, index) => (
                    <div className="tag" key={index}>
                      {entity.text} · {entity.type}
                    </div>
                  ))
                ) : (
                  <p>None detected</p>
                )}
              </div>

              <div className="result-card">
                <div className="card-icon">🔑</div>
                <h3>Key Phrases</h3>

                <div className="tags">
                  {result.key_phrases?.key_phrases?.map(
                    (phrase, index) => (
                      <span className="tag" key={index}>
                        {phrase}
                      </span>
                    )
                  )}
                </div>
              </div>

              <div className="result-card">
                <div className="card-icon">🔒</div>
                <h3>PII Detection</h3>

                {result.pii?.pii_detected?.length ? (
                  result.pii.pii_detected.map((item, index) => (
                    <div className="tag warning" key={index}>
                      {item.type}: {item.text}
                    </div>
                  ))
                ) : (
                  <p>None detected</p>
                )}
              </div>

              <div className="result-card">
                <div className="card-icon">🧠</div>
                <h3>Topics</h3>

                <div className="tags">
                  {result.topics?.topics?.map((topic, index) => (
                    <span className="tag" key={index}>
                      {topic}
                    </span>
                  ))}
                </div>
              </div>

              <div className="result-card">
                <div className="card-icon">📂</div>
                <h3>Content Aware</h3>

                <div className="tags">
                  {result.content_aware?.content_types?.map(
                    (type, index) => (
                      <span className="tag" key={index}>
                        {type}
                      </span>
                    )
                  )}
                </div>
              </div>

              <div className="result-card summary-card">
                <div className="card-icon">📝</div>
                <h3>Summary</h3>
                <p className="summary">
                  {result.summary?.summary}
                </p>
              </div>
            </div>
          </section>
        )}
      </main>

      <footer>
        <p>AI Text Analysis App • Built with React + FastAPI</p>
      </footer>
    </div>
  );
}

export default App;