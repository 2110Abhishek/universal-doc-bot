from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = (
    st.secrets["OPENAI_API_KEY"]
    if hasattr(st, "secrets") and "OPENAI_API_KEY" in st.secrets
    else os.getenv("OPENAI_API_KEY")
)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

class VectorDB:
    def __init__(self):
        self.db = None

    def build_store(self, chunks):
        if chunks:
            self.db = FAISS.from_texts(chunks, embeddings)

    def search(self, query, k=3):
        if not self.db:
            return []
        return self.db.similarity_search(query, k=k)
