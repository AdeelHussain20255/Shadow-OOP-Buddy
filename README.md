# Shadow — Java OOP Programming Buddy

An AI programming mentor inspired by Cid Kagenō / Shadow from *The Eminence in Shadow*, specialized as a **Java Object-Oriented Programming** teaching partner. It runs on the Mistral API and is available as a terminal chatbot and a Streamlit web interface.

## Features

- **Shadow persona** — a confident, composed, mysterious Java OOP mentor whose personality is defined in `SYSTEM_PROMPT.md`.
- **Java-first teaching** — Java is the default and primary language for all examples and explanations.
- **Terminal chatbot** — a simple, dependency-light command-line interface.
- **Streamlit frontend** — a chat-style UI with conversation history and a Clear Conversation control.
- **Runtime-loaded prompt** — the full system prompt is read from `SYSTEM_PROMPT.md` at startup; the persona is never hardcoded in application code.

## Tech stack

- **Python 3.12**
- **Mistral AI Python SDK** (`mistralai`)
- **Streamlit** (web UI)
- **python-dotenv** (`.env` loading)

## How the architecture works

```
app.py (Streamlit UI)
   │  UI only
   ▼
chatbot.py  ──  ShadowChat
   │            Mistral client + SYSTEM_PROMPT.md + conversation history
   ▼
Mistral API  →  Shadow's response
```

`chatbot.py` holds all shared logic in the `ShadowChat` class: it loads `SYSTEM_PROMPT.md` at runtime, holds the Mistral client, and maintains the in-memory conversation history. The terminal client (`chatbot.py` run directly) and the Streamlit frontend (`app.py`) both use the same class, so the API integration and system prompt live in exactly one place.

## Project structure

```
Shadow-OOP-Buddy/
├── chatbot.py           # shared ShadowChat logic + terminal client
├── app.py               # Streamlit UI (UI only)
├── SYSTEM_PROMPT.md     # the Shadow persona / system prompt (read at runtime)
├── requirements.txt     # Python dependencies
├── .env.example         # env var template (no secrets)
├── .gitignore           # ignores .env, .venv, __pycache__, etc.
└── AGENTS.md            # developer guidance for working in this repo
```

## Setup instructions

Requires Python 3.9+.

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt   # Windows
```

On macOS/Linux use `.venv/bin/python` instead of `.venv/Scripts/python.exe`.

## Environment variable setup

1. Copy the template:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and set your key:
   ```
   MISTRAL_API_KEY=your_key_here
   ```

Optional: override the default model with `MISTRAL_MODEL=mistral-large-latest`.

## How to run the Streamlit frontend

```bash
.venv/Scripts/python.exe -m streamlit run app.py
```

The app opens in your browser. History persists for the session via `st.session_state`; the Clear Conversation button resets it.

## How to run the terminal chatbot

```bash
.venv/Scripts/python.exe chatbot.py
```

Type `exit`, `quit`, `bye`, or `/exit` to leave.

## Prompt-engineering overview

`SYSTEM_PROMPT.md` defines the entire persona — `# 1. ROLE` through `# 29. FINAL PRIORITY`. Its core principle:

> Shadow's personality is the presentation layer. Java OOP expertise is the substance. Technical accuracy always wins, but the answer should still unmistakably feel like Shadow.

Key design decisions baked into the prompt:

- The **voice** carries the character (rhythm, confidence, framing) instead of catchphrases or repeated references to "shadows."
- Java is the default and center of expertise; other languages are not presented as equal specializations.
- Technical accuracy and learning value outrank dramatic presentation.
- The prompt teaches through original behavioral examples (concept explanations, debugging, design critique) rather than abstract rules alone.
- Guided assistance and hints are preferred over dropping complete solutions, unless the learner explicitly asks.

## Testing overview

There is no automated test suite yet. The project is verified with a smoke-check pattern:

- Modules import cleanly (`chatbot`, `app`).
- Missing `MISTRAL_API_KEY` exits gracefully with a clear message.
- The Streamlit app starts and serves locally when launched headless.

## Security note

Your Mistral API key lives **only** in `.env`, which is listed in `.gitignore` and never committed. Only `.env.example` (a keyless template) is tracked. Never commit a real API key, token, or secret to this repository.