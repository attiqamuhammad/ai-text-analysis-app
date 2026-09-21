from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Text to analyze"
    )