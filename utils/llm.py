import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = (
    st.secrets["OPENAI_API_KEY"]
    if hasattr(st, "secrets") and "OPENAI_API_KEY" in st.secrets
    else os.getenv("OPENAI_API_KEY")
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=OPENAI_API_KEY
)

def generate_answer(query, doc_context=None, web_context=None):
    prompt = f"""
You are a universal knowledge assistant.
Question: {query}
Document Context: {doc_context}
Web Context: {web_context}
Provide a clear, well-structured answer with sources.
"""
    return llm.predict(prompt)
