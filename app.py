import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

from utils.document_loader import load_and_chunk_pdf
from utils.vector_store import VectorDB
from utils.query_router import needs_web_search
from utils.web_search import web_search
from utils.llm import generate_answer

vector_db = VectorDB()

st.title("📄 Universal Document Intelligence Chatbot")

uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        chunks = load_and_chunk_pdf(file)
        vector_db.build_store(chunks)

query = st.text_input("Ask your question:")
if query:
    doc_context = vector_db.search(query) if vector_db.db else []
    web_context = None
    if needs_web_search(query):
        web_context = web_search(query)
    answer = generate_answer(query, doc_context, web_context)
    st.write(answer)
