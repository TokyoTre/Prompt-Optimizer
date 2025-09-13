

from prompt_optimizer import optimize_prompt, evaluate_prompt, PREDEFINED_PROMPTS, PREDEFINED_EVALUATIONS, INVALID_EVALUATION, DEFAULT_EVALUATION

# Define test cases
test_cases = [
    # Optimize Prompt Tests
    ('optimize_prompt', ('Write Python function',), PREDEFINED_PROMPTS['Write Python function']),
    ('optimize_prompt', ('Summarize data',), PREDEFINED_PROMPTS['Summarize data']),
    ('optimize_prompt', ('Translate text',), PREDEFINED_PROMPTS['Translate text']),
    ('optimize_prompt', ('Do it better',), "Do it better Please define the prompt more specifically."),
    ('optimize_prompt', ('',), "Please provide a valid prompt."),
    ('optimize_prompt', (None,), "Please provide a valid prompt."),
    ('optimize_prompt', (123,), "Please provide a valid prompt."),

    # Evaluate Prompt Tests
    ('evaluate_prompt', ('Write Python function',), PREDEFINED_EVALUATIONS['Write Python function']),
    ('evaluate_prompt', ('Summarize data',), PREDEFINED_EVALUATIONS['Summarize data']),
    ('evaluate_prompt', ('Translate text',), PREDEFINED_EVALUATIONS['Translate text']),
    ('evaluate_prompt', ('Do it better',), DEFAULT_EVALUATION),
    ('evaluate_prompt', ('',), INVALID_EVALUATION),
    ('evaluate_prompt', (None,), INVALID_EVALUATION),
    ('evaluate_prompt', (123,), INVALID_EVALUATION),
]

# Run tests
def run_tests():
    for func_name, args, expected in test_cases:
        func = globals().get(func_name)
        if not func:
            print(f"Function {func_name} not found!")
            continue
        try:
            result = func(*args)
            assert result == expected, f"❌ {func_name}{args} => {result}, expected {expected}"
            print(f"✅ {func_name}{args} passed")
        except AssertionError as e:
            print(str(e))
        except Exception as e:
            print(f"⚠️ {func_name}{args} raised {type(e)}")

if __name__ == "__main__":
    run_tests()
