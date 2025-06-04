def match_intent(query: str) -> str:
    query = query.lower()

    if "list" in query and "device" in query:
        return "list devices"
    if "ai" in query and ("channel" in query or "input" in query):
        return "get ai channels"
    if "ao" in query and ("channel" in query or "output" in query):
        return "get ao channels"
    if "di" in query and ("channel" in query or "input" in query):
        return "get di channels"
    if "do" in query and ("channel" in query or "output" in query):
        return "get do channels"

    return "unknown"
