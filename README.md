# Prompt Optimizer 🤖✍️

A Python module that **optimizes, evaluates, and stores natural language prompts**.
The Prompt Optimizer improves prompt clarity and specificity, evaluates prompt quality, and keeps a history of prompts for consistent AI interactions.

This project demonstrates how **predefined mappings + evaluation metrics + history tracking** can streamline prompt engineering for AI applications.

---

## ✨ Features
- **Prompt Optimization** – Automatically refine input prompts to be precise, clear, and actionable.
- **Prompt Evaluation** – Score prompts on clarity, specificity, completeness, and overall quality.
- **History Management** – Save/load prompt history in JSON files, avoiding duplicates.
- **Safe Handling** – Detects invalid or empty inputs and provides guidance.
- **Testing Utilities** – Includes built-in test cases for verification and debugging.

---

## 📂 Folder Structure
Prompt_Optimizer/
│── README.md # Project documentation
│── prompt_optimizer.py # Core implementation
│── test/ # Unit tests for optimizer and evaluator
│── docs/ # Design notes, examples, and methodology

---

## ⚙️ How It Works

1. **Input a Prompt** – Provide a natural language prompt.
2. **Optimization** – The module maps known prompts to improved versions.
3. **Evaluation** – Each prompt is scored on clarity, specificity, completeness, and overall quality.
4. **History Tracking** – Optimized prompts are saved to prompt_history.json to prevent duplicates.
5. **Result** – Return an optimized prompt along with its evaluation metrics.

---

## 🖥️ Example

**Input Prompt:**
prompt = "Write Python function"

Optimized Output:

"Write a Python function that takes input arguments as specified and produces correct output. Include docstrings and an example usage."


**Evaluation:**
{'clarity': 8, 'specificity': 7, 'completeness': 8, 'overall_score': 8}

Handling Invalid Input:

optimize_prompt("")  
# Output: "Please provide a valid prompt."

evaluate_prompt("")  
# Output: {'clarity': 0, 'specificity': 0, 'completeness': 0, 'overall_score': 0}


**Test Cases Format:**
- ('optimize_prompt', ('Do it better',), "Do it better Please define the prompt more specifically.")  
- ('evaluate_prompt', ('Do it better',), {'clarity': 5, 'specificity': 5, 'completeness': 5, 'overall_score': 5})


🔬 Use Cases:
- Improving AI prompt clarity for language models
- Rapid prototyping for data analysis, translation, or code generation prompts
- Automated evaluation and quality control of prompts in AI pipelines

🚧 Next Steps:
- Expand predefined prompt mappings
- Add dynamic AI-based optimization suggestions
- Integrate adaptive scoring with ML
- Build a CLI or web interface for easy prompt management

📜 License:

© 2025 Samuel Montgomery III. All rights reserved.

The Prompt Optimizer and all associated code, modules, documentation, and assets
are proprietary software owned exclusively by Samuel Montgomery III.

Permission is NOT granted to copy, modify, distribute, sell, sublicense,
or otherwise use this software, in whole or in part, without express written
consent from the copyright holder.

This software is provided "as-is" without any warranties, express or implied,
including but not limited to fitness for a particular purpose or non-infringement.

For inquiries regarding licensing or authorized use, contact:
sam.mont006@gmail.com
(252) 350-1541

👤 Author
- Developed by Samuel A. Montgomery, III
- AI Developer & Prompt Engineer (Freelance-ready)
- Certifications: Generative AI Leader Professional Certificate (Google Cloud), IBM AI Developer Professional Certificate, Python for Data Science, AI & Development Certificate (IBM), Google AI Essentials Specialization, Google Prompting Essentials Specialization, Generative AI for Customer Support Specialization (IBM).
