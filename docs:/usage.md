# Prompt Optimizer Usage Guide

---

## 🔧 Installation
```bash
git clone <repo-url>
cd Prompt_Optimizer
pip install -r requirements.txt
```


## ⚙️ Functions

optimize_prompt(prompt: str) -> str
Refines a prompt for clarity and specificity.

evaluate_prompt(prompt: str) -> dict
Returns a dictionary with keys: 'clarity', 'specificity', 'completeness', 'overall_score'.

save_history(data: Any, filename: str = "prompt_history.json") -> None
Saves prompt history to a JSON file, avoiding duplicates.

load_history(filename: str = "prompt_history.json") -> list
Loads saved prompt history from a JSON file.


## 🖥️ Example Usage

```python

from prompt_optimizer import optimize_prompt, evaluate_prompt

prompt = "Write Python function"
optimized = optimize_prompt(prompt)
evaluation = evaluate_prompt(prompt)

print(optimized)
print(evaluation)
```

## ✅ Advantages of this version:

- Clear section separation with `---`
- Bold function names for easy scanning
- Consistent spacing and headers
- Matches README.md styling conventions  
