ROUTING_KEYWORDS = [
    "latest", "current", "2024", "now", "vs", "alternatives", 
    "comparison", "price", "trend", "stock", "news", "explain", "how"
]

def needs_web_search(query):
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in ROUTING_KEYWORDS)
