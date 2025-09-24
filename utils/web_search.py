import requests
import os

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def web_search(query):
    url = "https://google.serper.dev/search"
    payload = {"q": query}
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
