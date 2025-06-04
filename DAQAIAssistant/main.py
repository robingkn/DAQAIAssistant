import os
import re
import requests

API_URL = "https://router.huggingface.co/hf-inference/models/HuggingFaceH4/zephyr-7b-beta/v1/chat/completions"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

if not HF_API_TOKEN:
    raise EnvironmentError("HF_API_TOKEN not set.")

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
}

MODEL = "HuggingFaceH4/zephyr-7b-beta"

def clean_code(code):
    # Extract the first Python code block
    code_blocks = re.findall(r"```(?:python)?\n([\s\S]*?)```", code, re.IGNORECASE)
    if code_blocks:
        cleaned = code_blocks[0].strip()
    else:
        cleaned = code.strip()

    # Remove decorators and leading blank lines
    lines = cleaned.splitlines()
    while lines and (lines[0].startswith('@') or lines[0].strip() == ''):
        lines.pop(0)

    # Optional: Trim after last line containing 'result'
    last_result_line = -1
    for i, line in enumerate(lines):
        if "result" in line:
            last_result_line = i
    if last_result_line != -1:
        lines = lines[:last_result_line + 1]

    cleaned = "\n".join(lines).strip()
    return cleaned

def get_python_code(user_query):
    system_msg = (
        "You are a helpful Python assistant. "
        "Only reply with runnable Python code, no explanations or comments. "
        "Do not define functions or decorators. "
        "The code must set the variable `result` as the output."
    )

    user_msg = (
        f"Write safe Python code that executes this request: {user_query}. "
        "The result must be assigned to a variable called `result`. "
        "Use the current working directory as default for any file operations."
    )

    payload = {
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        "model": MODEL
    }

    print("🎯 Asking the model...")
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()

    raw_code = response.json()["choices"][0]["message"]["content"]
    cleaned_code = clean_code(raw_code)
    return cleaned_code

def run_generated_code(code):
    try:
        local_vars = {}
        # Only expose os module for safety, you can expose more if needed
        exec(code, {"os": os}, local_vars)
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
