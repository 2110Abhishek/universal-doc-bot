import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the OpenAI chat model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",   # You can change to gpt-4 if you have access
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
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
