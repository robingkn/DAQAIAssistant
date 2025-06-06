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
    if "ci" in query and "channel" in query:
        return "get ci channels"
    if "co" in query and "channel" in query:
        return "get co channels"
    if "supported" in query and "measurement" in query:
        return "get supported measurement types"
    if "product" in query and "info" in query:
        return "get product info"

    return "unknown"
