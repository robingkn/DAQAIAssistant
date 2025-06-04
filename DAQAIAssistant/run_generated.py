# run_generated.py

def run_generated_code(code: str, client, nidaqmx_types, task=None):
    try:
        local_vars = {
            "client": client,
            "nidaqmx_types": nidaqmx_types,
            "task": task,
            "result": None,
        }
        exec(code, {}, local_vars)
        return local_vars.get("result"), local_vars.get("task")
    except Exception as e:
        return f"❌ Execution error: {e}", task
