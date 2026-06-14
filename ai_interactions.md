# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**
I gave both models the buggy check_guess function and asked them to find and fix the hint direction bug.
<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** |Gemini |Claude-Sonnet 4.6|
| **Response summary** |Caught the bug and swapped the hint messages immediately and explained how the code was giving opposite directions | Same fix, but also connected it to the type-switching bug and explained how both bugs together could break the win condition|
| **More Pythonic?** |Pretty much the same, as there's only one real way to fix swapped strings | A little better as gave the whole code in a downloadable python file |
| **Clearer explanation?** | A bit wordy as repeated the same point a few times|Got to the point faster and gave more useful context |

**Which did you prefer and why?**

I preferred Claude here mostly because it didn't just fix the one bug in only and pointed out how this bug and the type-switching bug were connected. This helped me understand the code better overall. Gemini was also correct but the explanations felt a bit long for what it was trying to explain.<!-- Your conclusion -->
