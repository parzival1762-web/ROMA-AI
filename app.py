import streamlit as st
from Roma import ask_roma

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Adrian AI",
    page_icon="❤️",
    layout="centered"
)

# -----------------------------
# Session State
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Welcome Page
# -----------------------------
if st.session_state.page == "welcome":

    st.title("❤️ Roma AI")

    st.markdown("## Your Personal AI Companion")

    st.write("")

    st.markdown("""
Welcome to **Roma AI**.

Chat with Roma about anything.

- 💬 Ask questions
- ❤️ Have conversations
- 🤖 Made by Romee with lots of love
""")

    st.write("")

    if st.button("🚀 Start Chatting", use_container_width=True):
        st.session_state.page = "chat"
        st.rerun()

# -----------------------------
# Chat Page
# -----------------------------
elif st.session_state.page == "chat":

    col1, col2 = st.columns([8, 2])

    with col1:
        st.title("❤️ Adrian AI")

    with col2:
        if st.button("🏠 Home"):
            st.session_state.page = "welcome"
            st.rerun()

    # Show previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input("Message Roma...")

    if prompt:

        # Show user's message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # Thinking animation
        with st.spinner("Roma is thinking..."):

            reply = ask_roma(prompt)

        # Save AI reply
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        # Show AI reply
        with st.chat_message("assistant"):
            st.markdown(reply)