import uuid
import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖")

st.title("LangGraph Chatbot")

# Create unique thread_id for this browser session
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

CONFIG = {
    "configurable": {
        "thread_id": st.session_state["thread_id"]
    }
}

# Store UI-visible messages
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# Load previous Streamlit UI messages
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type here")

if user_input:
    # Add user message to Streamlit UI history
    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Invoke LangGraph chatbot
    response = chatbot.invoke(
        {
            "messages": [HumanMessage(content=user_input)]
        },
        config=CONFIG
    )

    ai_message = response["messages"][-1].content

    # Add assistant message to Streamlit UI history
    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })

    with st.chat_message("assistant"):
        st.markdown(ai_message)