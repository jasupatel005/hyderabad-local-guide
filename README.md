
# Hyderabad Local Guide — Agent-Steered Tool (Kiro + `product.md`)

A complete, ready-to-upload project for **The Local Guide Challenge**. This repo demonstrates **Agent Steering** using a custom context file at `/.kiro/product.md` to teach *Kiro* Hyderabad-specific nuances.

## What This Includes
- `/.kiro/product.md`: The authoritative local context used to steer the agent.
- `src/app.py`: A **Streamlit** app featuring:
  - **Slang Translator** (Hyderabad slang → standard English)
  - **Traffic Estimator** (rule-based + context-driven)
  - **Local Tips** (food, safety, cultural notes)
- `src/context_loader.py`: Utility to parse `product.md` and expose the structured context.
- `tests/test_context.py`: Basic tests to validate context parsing.
- `assets/` screenshots placeholder and recording instructions for your blog.

## Quick Start
```bash
# 1) Create env
python -m venv .venv && . .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the app
streamlit run src/app.py
```

Open the app at the URL Streamlit prints (usually http://localhost:8501). Take screenshots/GIFs for the AWS Builder Center blog.

## How Agent Steering Works Here
Kiro looks for the `/.kiro` directory. We store Hyderabad-specific knowledge in `product.md` and the app reads from it via `src/context_loader.py`. All decisions (translations, traffic heuristics, local tips) fetch rules from the parsed context—**no generic defaults** unless explicitly allowed. Update `product.md` to steer behavior.

## Project Structure
```
hyderabad-local-guide/
├── .kiro/
│   ├── product.md
├── src/
│   ├── app.py
│   ├── context_loader.py
├── tests/
│   ├── test_context.py
├── assets/
│   ├── README.md
├── requirements.txt
├── LICENSE
├── README.md
```

## Blog Help (AWS Builder Center)
Use the `Blog Outline` below as a template.

### Blog Outline
1. **Intro**: The Local Guide Challenge & goal
2. **Agent Steering Concept**: Why custom context, how `product.md` directs Kiro
3. **Design**: Repo layout, parsing pipeline, modules
4. **Feature Deep-Dive**: Slang, Traffic, Tips — each with screenshots/GIFs
5. **Context Snippets**: Include YAML from `product.md`
6. **Evaluation**: Edge cases and how context improves responses
7. **How-To**: Run locally, extend to other cities
8. **Conclusion**: Lessons + call-to-action

## Notes
- Replace or expand `/.kiro/product.md` for other cities.
- This repo is intentionally self-contained and does not require external APIs.
- License: MIT (see `LICENSE`).
