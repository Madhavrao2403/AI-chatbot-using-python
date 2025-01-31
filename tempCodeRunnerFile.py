import streamlit as st
import os
import google.generativeai as ai
from dotenv import load_dotenv

st.set_page_config(page_icon="💬", page_title="ChatBot(LLM)",layout="centered")

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

ai.configure(api_key=GOOGLE_API_KEY)
model = ai.GenerativeModel('gemini-pro')

def translate(role):
    return "assistant" if role == "model" else role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Basic LLM ChatBot💬")
st.subheader("This is a basic chatbot using the Gemini API Pro")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate(message.role)):
        st.markdown(message.parts[0].text)

user_input = st.chat_input("Message ChatBot")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    
    gemini_response = st.session_state.chat_session.send_message(user_input)
    
    with st.chat_message("assistant"):
        st.markdown(gemini_response.candidates[0].content.parts[0].text)
