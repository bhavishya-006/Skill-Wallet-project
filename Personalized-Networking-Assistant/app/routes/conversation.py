from fastapi import APIRouter

from app.models.schemas import (
    ConversationRequest,
    ConversationResponse,
    ThemeResponse,
    FactCheckRequest,
    FactCheckResponse
)

from app.services.event_analyzer import extract_event_themes
from app.services.topic_generator import generate_topics
from app.services.fact_checker import fact_check
from app.services.history_logger import log_conversation

router = APIRouter()


@router.post("/analyze-event", response_model=ThemeResponse)
def analyze_event(request: ConversationRequest):
    themes = extract_event_themes(request.description)

    return {
        "themes": themes
    }


@router.post("/fact-check", response_model=FactCheckResponse)
def check_fact(request: FactCheckRequest):

    summary = fact_check(request.query)

    return {
        "summary": summary
    }


@router.post("/generate-conversation", response_model=ConversationResponse)
def generate_conversation(request: ConversationRequest):

    topics = extract_event_themes(request.description)

    suggestions = generate_topics(
        topics,
        request.interests
    )

    log_conversation({
        "description": request.description,
        "topics": topics,
        "suggestions": suggestions
    })

    return {
        "topics": topics,
        "suggestions": suggestions
    }