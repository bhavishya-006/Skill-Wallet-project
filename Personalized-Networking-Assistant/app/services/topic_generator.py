from transformers import pipeline, set_seed

# Load GPT-2 text generation model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Set seed for reproducible outputs
set_seed(42)


def generate_topics(event_themes, user_interests):
    """
    Generate conversation starters based on event themes
    and user interests.
    """

    prompt = (
        f"I am attending a networking event focused on "
        f"{', '.join(event_themes)}.\n"
        f"My interests are {', '.join(user_interests)}.\n"
        f"Generate three professional conversation starters:\n"
    )

    result = generator(
        prompt,
        max_length=80,
        num_return_sequences=1,
        truncation=True
    )

    generated_text = result[0]["generated_text"]

    suggestions = generated_text.split("\n")

    cleaned = []

    for line in suggestions:
        line = line.strip("-• ").strip()

        if line and line != prompt:
            cleaned.append(line)

    return cleaned[:3]