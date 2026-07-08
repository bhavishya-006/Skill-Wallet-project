from pydantic import BaseModel
from typing import List

class ConversationRequest(BaseModel):
    description: str
    interests: List[str]

class ThemeResponse(BaseModel):
    themes: List[str]

class ConversationResponse(BaseModel):
    topics: List[str]
    suggestions: List[str]

class FactCheckRequest(BaseModel):
    query: str

class FactCheckResponse(BaseModel):
    summary: str

class FeedbackRequest(BaseModel):
    suggestion: str
    action: str