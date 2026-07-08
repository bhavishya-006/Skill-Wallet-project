import json
from pathlib import Path
from datetime import datetime

# File where conversation history will be stored
HISTORY_FILE = Path("conversation_history.json")


def log_conversation(data: dict):
    """
    Saves a conversation to the history file.
    """

    data["timestamp"] = datetime.now().isoformat()

    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    else:
        history = []

    history.append(data)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def load_history():
    """
    Loads all saved conversations.
    """

    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    return []