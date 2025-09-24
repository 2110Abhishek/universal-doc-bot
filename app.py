import streamlit as st
from dotenv import load_dotenv
import os

# Load .env locally
load_dotenv()

from utils.document_loader import load_and_chunk_pdf
from utils.vector_store import VectorDB
from utils.query_router import needs_web_search
from utils.web_search import web_search
from utils.llm import generate_answer

# Initialize vector database
vector_db = VectorDB()

st.title("📄 Universal Document Intelligence Chatbot")

# Upload PDFs
uploaded_files = st.file_uploader(
    "Upload PDFs", type=["pdf"], accept_multiple_files=True
)
if uploaded_files:
    for file in uploaded_files:
        chunks = load_and_chunk_pdf(file)
        vector_db.build_store(chunks)
    st.success(f"{len(uploaded_files)} file(s) processed and added to vector store.")

# User query input
query = st.text_input("Ask your question:")

if query:
    # Search vector DB
    doc_context = vector_db.search(query) if vector_db.db else []
    
    # Optional web search context
    web_context = web_search(query) if needs_web_search(query) else None
    
    # Generate answer
    answer = generate_answer(query, doc_context, web_context)
    
    st.subheader("Answer:")
    st.write(answer)
