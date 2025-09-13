import json
import os
from typing import Any, Dict

# -------------------------
# Prompt Optimizer & Evaluator
# -------------------------

PROMPT_HISTORY_FILE = "prompt_history.json"
CONVERSATION_HISTORY_FILE = "conversation_history.json"

# Predefined mappings for optimization
PREDEFINED_PROMPTS = {
    "Write Python function": "Write a Python function that takes input arguments as specified and produces correct output. Include docstrings and an example usage.",
    "Summarize data": "Summarize the data clearly and concisely, including key metrics and actionable insights. Include example output.",
    "Translate text": "Translate the given text accurately and fluently, preserving meaning and context. Include example translation.",
}

# Predefined evaluations
PREDEFINED_EVALUATIONS = {
    "Write Python function": {'clarity': 8, 'specificity': 7, 'completeness': 8, 'overall_score': 8},
    "Summarize data": {'clarity': 9, 'specificity': 8, 'completeness': 8, 'overall_score': 8},
    "Translate text": {'clarity': 8, 'specificity': 9, 'completeness': 7, 'overall_score': 8},
}

DEFAULT_EVALUATION = {'clarity': 5, 'specificity': 5, 'completeness': 5, 'overall_score': 5}
INVALID_EVALUATION = {'clarity': 0, 'specificity': 0, 'completeness': 0, 'overall_score': 0}

# -------------------------
# Core Functions
# -------------------------

def optimize_prompt(prompt: Any) -> str:
    """
    Optimize a given prompt using predefined mappings.
    
    Returns:
        str: Optimized prompt, or guidance message if unmapped/invalid.
    """
    if not isinstance(prompt, str) or not prompt.strip():
        return "Please provide a valid prompt."
    prompt = prompt.strip()
    return PREDEFINED_PROMPTS.get(prompt, f"{prompt} Please define the prompt more specifically.")

def evaluate_prompt(prompt: Any) -> Dict[str, int]:
    """
    Evaluate the quality of a prompt using predefined scores.
    
    Returns:
        dict: Evaluation dictionary with keys 'clarity', 'specificity', 'completeness', 'overall_score'.
    """
    if not isinstance(prompt, str) or not prompt.strip():
        return INVALID_EVALUATION
    prompt = prompt.strip()
    return PREDEFINED_EVALUATIONS.get(prompt, DEFAULT_EVALUATION)

# -------------------------
# History Handling
# -------------------------

def save_history(data: Any, filename: str = PROMPT_HISTORY_FILE) -> None:
    """
    Save data to a JSON file, preventing duplicates. Auto-creates file if missing.
    """
    if not os.path.exists(filename):
        existing_data = []
    else:
        try:
            with open(filename, 'r') as f:
                existing_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            existing_data = []

    if data not in existing_data:
        existing_data.append(data)
    
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)

def load_history(filename: str = PROMPT_HISTORY_FILE) -> list:
    """
    Load saved prompt history from file.
    """
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# -------------------------
# Testing Utilities
# -------------------------

def run_tests(test_cases: list) -> None:
    """
    Run test cases on optimizer/evaluator functions.
    """
    for func_name, args, expected in test_cases:
        func = globals().get(func_name)
        if not func:
            print(f"Function {func_name} not found!")
            continue
        try:
            result = func(*args)
            assert result == expected, f"❌ {func_name}{args} => {result}, expected {expected}"
            print(f"✅ {func_name}{args} passed")
        except Exception as e:
            print(f"⚠️ {func_name}{args} raised {e}")

# -------------------------
# Example Test Cases
# -------------------------

test_cases = [
    ('optimize_prompt', ('Write Python function',), PREDEFINED_PROMPTS['Write Python function']),
    ('optimize_prompt', ('Do it better',), "Do it better Please define the prompt more specifically."),
    ('optimize_prompt', ('',), "Please provide a valid prompt."),
    ('optimize_prompt', (None,), "Please provide a valid prompt."),
    ('evaluate_prompt', ('Summarize data',), PREDEFINED_EVALUATIONS['Summarize data']),
    ('evaluate_prompt', ('Do it better',), DEFAULT_EVALUATION),
    ('evaluate_prompt', ('',), INVALID_EVALUATION),
]

# -------------------------
# Main Execution
# -------------------------

if __name__ == "__main__":
    run_tests(test_cases)

