from app.services.feedback_logger import log_feedback, load_feedback

log_feedback(
    "Hi! What inspired you to work in AI?",
    "like"
)

print(load_feedback())