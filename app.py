import streamlit as st

from utils.prompt_loader import load_system_prompt
from agent.agent_service import ask_agent

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": load_system_prompt()
        }
    ]

# Display chat history
for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input(
    "Ask anything..."
)

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Agent handles request
    response = ask_agent(user_input)

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )