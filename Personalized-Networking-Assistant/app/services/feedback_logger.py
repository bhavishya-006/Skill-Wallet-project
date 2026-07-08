import json
from pathlib import Path
from datetime import datetime

# File where feedback will be stored
FEEDBACK_FILE = Path("feedback_history.json")


def log_feedback(suggestion: str, action: str):
    """
    Saves user feedback to the feedback file.
    """

    feedback = {
        "suggestion": suggestion,
        "action": action,
        "timestamp": datetime.now().isoformat()
    }

    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(feedback)

    with open(FEEDBACK_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_feedback():
    """
    Loads all feedback entries.
    """

    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, "r") as file:
            return json.load(file)

    return []