from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os

# Use environment variable explicitly
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

class VectorDB:
    def __init__(self):
        self.db = None

    def build_store(self, chunks):
        self.db = FAISS.from_texts(chunks, embeddings)

    def search(self, query, k=3):
        return self.db.similarity_search(query, k=k)
