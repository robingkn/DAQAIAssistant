import json
import os

def load_intent_map(filename="intent_map.json"):
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r") as f:
        return json.load(f)
