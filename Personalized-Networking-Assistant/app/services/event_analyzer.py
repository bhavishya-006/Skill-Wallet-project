from transformers import pipeline

# Load the zero-shot classification model only once when the application starts
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)


def extract_event_themes(description: str, candidate_labels=None):
    """
    Extracts the top three themes from an event description.
    """

    if candidate_labels is None:
        candidate_labels = [
            "Artificial Intelligence",
            "Machine Learning",
            "Blockchain",
            "Healthcare",
            "Cybersecurity",
            "Cloud Computing",
            "Education",
            "Finance",
            "Startups",
            "Data Science",
            "Networking",
            "Sustainability"
        ]

    result = classifier(description, candidate_labels)

    return result["labels"][:3]