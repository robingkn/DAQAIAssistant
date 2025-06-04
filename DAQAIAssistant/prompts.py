# prompts.py

def grpc_prompt_template(user_instruction: str) -> str:
    return f"""
You are an AI assistant that writes safe Python code to control NI DAQ devices using gRPC.

Context:
- grpc client instance is `client` (of type NiDAQmxStub)
- task object is a string named `task` created with client.CreateTask(...)
- Protocol buffer messages come from `nidaqmx_types` (e.g., nidaqmx_types.CreateTaskRequest)
- Handle warnings using client.GetErrorString if response.status > 0
- Assign the final output to a variable named `result`

Write Python code to: {user_instruction}

Return only the code. Don't include explanations or comments. Ensure variable `result` is defined.
"""
