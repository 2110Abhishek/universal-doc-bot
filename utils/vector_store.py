from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os
import streamlit as st
from dotenv import load_dotenv

# Load .env locally
load_dotenv()

# Use Streamlit secret if available, else fallback to .env
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# Initialize embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

class VectorDB:
    def __init__(self):
        self.db = None

    def build_store(self, chunks):
        # Build FAISS vector store from text chunks
        self.db = FAISS.from_texts(chunks, embeddings)

    def search(self, query, k=3):
        if not self.db:
            return []
        return self.db.similarity_search(query, k=k)
