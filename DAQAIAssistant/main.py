import json
import nidaqmx
from nidaqmx.system import System
from nidaqmx.constants import LineGrouping

# --- Load intent map ---
with open("intent_map.json") as f:
    intent_api_map = json.load(f)

# --- Rule-based intent matcher ---
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

# --- Real NI-DAQmx API functions ---
def list_nidaq_devices():
    system = System.local()
    print("Connected Devices:")
    for device in system.devices:
        print(f"  {device.name}")

def get_ai_channels():
    for device in System.local().devices:
        print(f"{device.name} AI Channels: {device.ai_physical_chans.channel_names}")

def get_ao_channels():
    for device in System.local().devices:
        print(f"{device.name} AO Channels: {device.ao_physical_chans.channel_names}")

def get_di_channels():
    for device in System.local().devices:
        print(f"{device.name} DI Channels: {device.di_lines.channel_names}")

def get_do_channels():
    for device in System.local().devices:
        print(f"{device.name} DO Channels: {device.do_lines.channel_names}")

# Basic stateful task example
task = None

def start_ai_task():
    global task
    device = list(System.local().devices)[0].name
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan(f"{device}/ai0")
    task.start()
    print(f"Started AI task on {device}/ai0")

def stop_task():
    global task
    if task:
        task.stop()
        task.close()
        print("Task stopped and closed.")
    else:
        print("No active task.")

# --- Chat loop ---
def run_chatbot():
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

# --- Run bot ---
if __name__ == "__main__":
    run_chatbot()
