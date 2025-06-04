# main.py

import openai_key
from prompts import SYSTEM_PROMPT, get_user_prompt
from run_generated import run_generated_code
import nidaqmx_pb2 as nidaqmx_types
import nidaqmx_pb2_grpc as grpc_nidaqmx
import grpc
import requests

# Setup gRPC client
SERVER_ADDRESS = "localhost:31763"
channel = grpc.insecure_channel(SERVER_ADDRESS)
client = grpc_nidaqmx.NiDAQmxStub(channel)
task = None

def call_model(prompt):
    print("🎯 Asking the model...")
    response = requests.post(openai_key.API_URL, headers=openai_key.HEADERS, json={
        "messages": [{"role": "user", "content": prompt}],
        "model": "HuggingFaceH4/zephyr-7b-beta"
    })
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def main():
    global task
    print("📡 DAQ gRPC Assistant (type 'exit' to quit)")
    while True:
        user_input = input("🟦 You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break

        prompt = get_user_prompt(user_input)
        code = call_model(prompt)
        print("\n📝 Code generated:\n", code)

        result, task = run_generated_code(code, client, nidaqmx_types, task)
        print("\n✅ Result:\n", result, "\n")

if __name__ == "__main__":
    main()
