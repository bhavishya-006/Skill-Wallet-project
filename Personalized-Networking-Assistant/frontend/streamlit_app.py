import streamlit as st
import requests

st.title("🤝 Personalized Networking Assistant")

event = st.text_area("Event Description")

interests = st.text_input("Your Interests (comma separated)")

if st.button("Generate Conversation"):

    data = {
        "description": event,
        "interests": [i.strip() for i in interests.split(",")]
    }

    response = requests.post(
        "http://127.0.0.1:8000/generate-conversation",
        json=data
    )

    if response.status_code == 200:

        result = response.json()

        st.subheader("📌 Event Topics")
        for topic in result["topics"]:
            st.write("•", topic)

        st.subheader("💬 Conversation Suggestions")
        for suggestion in result["suggestions"]:
            st.write("•", suggestion)

    else:
        st.error(response.text)
    st.write(result)