from app.services.event_analyzer import extract_event_themes

description = "An AI conference discussing machine learning and cloud computing."

themes = extract_event_themes(description)

print(themes)
