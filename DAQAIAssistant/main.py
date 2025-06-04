import grpc
from openai import OpenAI
import nidaqmx_pb2
import nidaqmx_pb2_grpc
from run_generated import run_generated_code
from prompts import get_prompt

# Initialize OpenAI client (uses OPENAI_API_KEY env variable)
client = OpenAI()

def get_code_from_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    content = response.choices[0].message.content
    return content.removeprefix("```python").removesuffix("```").strip()

def main():
    channel = grpc.insecure_channel("localhost:31763")
    stub = nidaqmx_pb2_grpc.NiDAQmxStub(channel)

    print("💬 NI-DAQ Chat Interface (type 'exit' to quit)")
    while True:
        query = input("🧑 You: ").strip()
        if query.lower() in {"exit", "quit"}:
            break

        prompt = get_prompt(query)
        generated_code = get_code_from_openai(prompt)

        print("\n🤖 Generated Code:\n" + generated_code)
        print("\n🚀 Executing...\n")
        result = run_generated_code(generated_code, {
            "stub": stub,
            "nidaqmx_pb2": nidaqmx_pb2
        })
        print("📤 Result:\n", result, "\n")

if __name__ == "__main__":
    main()
