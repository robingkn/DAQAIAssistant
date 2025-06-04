import os
import requests

API_URL = "https://router.huggingface.co/nebius/v1/chat/completions"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

if not HF_API_TOKEN:
    raise EnvironmentError("HF_API_TOKEN not set.")

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
}

MODEL = "deepseek-ai/DeepSeek-R1-0528"

def get_python_code(prompt):
    print("🎯 Asking the model...")
    response = requests.post(API_URL, headers=HEADERS, json={
        "messages": [{"role": "user", "content": f"Write safe Python code to {prompt}. Return result in a variable named `result`."}],
        "model": MODEL
    })
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def run_generated_code(code):
    try:
        local_vars = {}
        exec(code, {"os": os}, local_vars)  # expose os module safely
        return local_vars.get("result", "No result variable defined.")
    except Exception as e:
        return f"❌ Execution error: {e}"

def main():
    print("📂 Filesystem Assistant (type 'exit' to quit)")
    while True:
        user_input = input("🟦 You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break

        code = get_python_code(user_input)
        print("\n📝 Code generated:\n", code)

        result = run_generated_code(code)
        print("\n✅ Result:\n", result, "\n")

if __name__ == "__main__":
    main()
