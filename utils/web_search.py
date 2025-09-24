import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = (
    st.secrets["SERPER_API_KEY"]
    if hasattr(st, "secrets") and "SERPER_API_KEY" in st.secrets
    else os.getenv("SERPER_API_KEY")
)

def web_search(query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    payload = {"q": query}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
