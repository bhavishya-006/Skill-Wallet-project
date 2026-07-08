from app.services.topic_generator import generate_topics

themes = [
    "Artificial Intelligence",
    "Machine Learning"
]

interests = [
    "Python",
    "Deep Learning"
]

result = generate_topics(themes, interests)

print(result)
