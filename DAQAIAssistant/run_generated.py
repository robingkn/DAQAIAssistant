def run_generated_code(code: str, context: dict):
    try:
        exec_globals = {}
        exec_locals = context.copy()
        exec(code, exec_globals, exec_locals)
        return exec_locals.get("result", "No result variable found in code.")
    except Exception as e:
        return f"Error executing code: {e}"
