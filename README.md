# agentic-workshop

Working repo for the **Agentic AI Workshop 2026** (University of Essex, 1–2 October 2026).
Capstone: Project 3 — Market & Competitor Intelligence Agent (Group C).

## How this repo is used

Logic lives in `src/agentic_workshop/` as plain `.py` modules. Notebooks stay thin —
they import from `src` and run things. Notebooks merge badly, `.py` files don't.

```
src/agentic_workshop/   shared code (imported by the notebooks)
notebooks/              lab and capstone notebooks
requirements.txt        packages the labs need
.env.example            secret names — copy to .env locally, never commit .env
```

## Colab bootstrap

First cell of every notebook. Works on a fresh runtime and on a re-run:

```python
import os, sys
if os.path.exists('/content/agentic-workshop'):
    !cd /content/agentic-workshop && git pull
else:
    !git clone https://github.com/jb1704/agentic-workshop.git /content/agentic-workshop
sys.path.insert(0, '/content/agentic-workshop/src')
!pip install -q -r /content/agentic-workshop/requirements.txt
```

After pulling new code mid-session, either restart the runtime or reload the module:

```python
import importlib, agentic_workshop
importlib.reload(agentic_workshop)
```

## Secrets

Never paste an API key into a notebook cell — it gets committed and shared.

- **Colab:** key icon in the left sidebar → Secrets → add `OPENAI_API_KEY` etc.
- **Local:** copy `.env.example` to `.env` and fill it in. `.env` is gitignored.

Read them the same way in both places:

```python
from agentic_workshop import get_secret
api_key = get_secret("OPENAI_API_KEY")
```

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
