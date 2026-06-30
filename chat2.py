import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

st.title("Groq Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Type your message...")

if user_input:
  
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    messages = [
        msg["content"]
        for msg in st.session_state.chat_history
    ]

    
    result = model.invoke(messages)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": result.content}
    )

   
    with st.chat_message("assistant"):
        st.write(result.content) 