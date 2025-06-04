# intent_router.py

def match_intent(query: str) -> str:
    query = query.lower()

    if "list" in query and "device" in query:
        return "list devices"
    if "analog input" in query or "ai channel" in query:
        return "get ai channels"
    if "analog output" in query or "ao channel" in query:
        return "get ao channels"
    if "digital input" in query or "di channel" in query:
        return "get di channels"
    if "digital output" in query or "do channel" in query:
        return "get do channels"
    if "start" in query and "analog input" in query:
        return "start analog input"
    if "stop" in query and "task" in query:
        return "stop task"
    
    return "unknown"
