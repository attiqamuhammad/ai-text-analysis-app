from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Backend.models import AnalysisRequest
from Backend.services.sentiment import analyze_sentiment
from Backend.services.tone import analyze_tone
from Backend.services.safety import analyze_safety
from Backend.services.ner import analyze_ner
from Backend.services.key_phrases import extract_key_phrases
from Backend.services.pii import analyze_pii
from Backend.services.summary import generate_summary
from Backend.services.topics import extract_topics
from Backend.services.content_aware import analyze_content_aware
from Backend.agent.orchestrator import analyze_text_with_agent


app = FastAPI(
    title="AI Text Analysis API",
    description="AI-powered text analysis application",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
)
allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://ai-text-analysis-app.vercel.app",
]
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],


@app.get("/")
def root():
    return {
        "message": "AI Text Analysis API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze_text(request: AnalysisRequest):
    sentiment_result = analyze_sentiment(request.text)
    tone_result = analyze_tone(request.text)
    safety_result = analyze_safety(request.text)
    ner_result = analyze_ner(request.text)
    key_phrases_result = extract_key_phrases(request.text)
    pii_result = analyze_pii(request.text)
    summary_result = generate_summary(request.text)
    topics_result = extract_topics(request.text)
    content_aware_result = analyze_content_aware(request.text)

    return {
        "sentiment": sentiment_result,
        "tone": tone_result,
        "safety": safety_result,
        "ner": ner_result,
        "key_phrases": key_phrases_result,
        "pii": pii_result,
        "summary": summary_result,
        "topics": topics_result,
        "content_aware": content_aware_result,
    }

@app.post("/analyze-agent")
def analyze_with_agent(request: AnalysisRequest):
    return analyze_text_with_agent(request.text)