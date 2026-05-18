import streamlit as st
from services.gemini_services import generate_response

# Page Configuration
st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("🤖 AI Career Assistant Chatbot")

st.markdown("""
Welcome to the AI Career Assistant Chatbot.

You can ask:
- AI/ML concepts
- Resume tips
- Interview questions
- Career guidance
- Project ideas
""")

# Sidebar
with st.sidebar:
    st.header("📌 Features")

    st.write("✅ Gemini GenAI API")
    st.write("✅ Prompt Engineering")
    st.write("✅ Modular Architecture")
    st.write("✅ Streamlit UI")
    st.write("✅ Conversation History")

    # Clear Chat Button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Display Previous Messages
for chat in st.session_state.chat_history:

    with st.chat_message("user"):
        st.markdown(chat["user"])

    with st.chat_message("assistant"):
        st.markdown(chat["assistant"])

# User Input
user_input = st.chat_input("Type your message here...")

# Generate Response
if user_input:

    # Show User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI Response
    with st.spinner("Generating response..."):

        response = generate_response(
            user_input,
            st.session_state.chat_history
        )

    # Show Assistant Message
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save Conversation
    st.session_state.chat_history.append({
        "user": user_input,
        "assistant": response
    })