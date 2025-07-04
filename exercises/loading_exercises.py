import json
from typing import List

def get_exercises(filename="exercises.json") -> List[str]:
    """Load exercises from a JSON file and return them as a list."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading exercises: {e}")
        return []