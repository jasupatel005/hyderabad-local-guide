
# Steering Kiro with `product.md`: Building a Hyderabad Local Guide

**Author:** Your Name  
**Platform:** AWS Builder Center  
**Repo:** (link to your public GitHub repo)

## Overview
We built a city-aware tool for Hyderabad that understands slang, traffic patterns, and cultural tips—**steered entirely by a custom context file** `/.kiro/product.md`.

## Why Agent Steering?
Generic agents miss local nuance. By placing authoritative knowledge in `/.kiro/product.md`, the agent uses rules and mappings sourced directly from your dataset.

## Architecture
```
.kiro/product.md  <-- Local context (YAML blocks in Markdown)
src/context_loader.py  <-- Parses product.md
src/app.py  <-- Streamlit UI calling context APIs
```

## Using `product.md`
We embed YAML blocks inside Markdown so writers can document and engineers can parse. Example:
```yaml
slang:
  - word: pakka
    meaning: sure
```

## Features & Demos
- **Slang Translator** → screenshot
- **Traffic Estimator** → screenshot
- **Local Tips** → screenshot

## Evidence (Visuals)
Include 3–5 screenshots or a short GIF of the app performing translations and estimations.

## How to Run
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```

## Extending to Other Cities
Duplicate `.kiro/product.md` and replace the YAML with the target city’s data.

## Conclusion
Agent Steering with `product.md` cleanly separates local knowledge from code. This design produces **auditable**, **update-friendly** tools.
