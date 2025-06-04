def get_prompt(user_query):
    return f"""
You are an assistant generating Python code to interact with a gRPC NI-DAQmx API.

Use only the provided objects:
- stub: gRPC client
- nidaqmx_pb2: protobuf module

Your code MUST assign the final output to a variable named 'result'.

Example:
devices = stub.GetSysDevNames(nidaqmx_pb2.GetSysDevNamesRequest()).device_names
result = [{{"name": dev}} for dev in devices]

User Query: "{user_query}"

Now generate Python code:
"""
