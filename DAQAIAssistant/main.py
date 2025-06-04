import os
import requests

# Use a lightweight free model (e.g., gpt2)
HF_MODEL_ID = "tiiuae/falcon-7b-instruct"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

def get_code_from_huggingface(prompt: str) -> str:
    if not HF_API_TOKEN:
        raise EnvironmentError("Set HF_API_TOKEN in your environment.")

    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7,
            "return_full_text": False,
        }
    }

    url = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, dict) and "error" in data:
        raise RuntimeError(f"Hugging Face Error: {data['error']}")

    return data[0]["generated_text"]

def run_generated_code(code: str) -> str:
    try:
        local_vars = {}
        exec(code, {}, local_vars)
        return str(local_vars.get("result", "✅ Code ran successfully"))
    except Exception as e:
        return f"❌ Error during execution: {e}"

def main():
    print("🎯 Type your DAQ-like query (or 'exit' to quit)")
    while True:
        query = input("🔹 You: ").strip()
        if query.lower() in {"exit", "quit"}:
            break

        prompt = f"Write Python code to {query}. Output should assign a variable 'result'."
        print("🧠 Thinking...")
        code = get_code_from_huggingface(prompt)
        print("\n📝 Code:\n", code)

        print("\n🚀 Running...")
        output = run_generated_code(code)
        print("\n📤 Output:\n", output)

if __name__ == "__main__":
    main()
