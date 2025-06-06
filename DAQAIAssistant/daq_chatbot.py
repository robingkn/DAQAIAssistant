from intent_router import match_intent
from nidaq_grpc_handlers import *
from intent_loader import load_intent_map

def run_chatbot():
    intent_api_map = load_intent_map()
    print("🟢 NI-DAQmx Chatbot ready. Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.strip().lower() == "exit":
            break

        intent = match_intent(query)
        func_name = intent_api_map.get(intent)

        if func_name and func_name in globals():
            try:
                globals()[func_name]()
            except Exception as e:
                print(f"⚠️ Error during execution: {e}")
        else:
            print("🤖 Sorry, I didn't understand that.")
