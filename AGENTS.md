# AGENTS.md

## What this repo is

**Shadow-Garden** is a prompt-engineering project: it defines the persona **Shadow** — an AI programming mentor inspired by Cid Kagenō / Shadow from *The Eminence in Shadow*, specialized as an OOP buddy/mentor.

The persona is defined in `SYSTEM_PROMPT.md` as a single 52-section prompt (sections `# 1. IDENTITY` through `# 52. FINAL OPERATING PRINCIPLE`). Its core principle: Shadow's personality is the presentation layer; Java OOP expertise is the substance. It is **Java-only** — Java is the default and primary language.

## Working conventions

- `SYSTEM_PROMPT.md` is a single document, not staged batches. Edit it in place and keep the `# N. TITLE` section numbering intact. The chatbot reads it at runtime; never inline prompt content into Python. Substantive prompt changes require asking the user first.
- Preserve the fixed persona constraints when generating or editing prompt content. Non-negotiable rules an agent must not break:
  - Technical accuracy is non-negotiable; never sacrifice correctness for dramatic style (sections 13, 29, 52).
  - Sound like Shadow without announcing it — no catchphrase spam, forced shadow metaphors, or "as an AI" filler (sections 3, 4, 18, 50).
  - Treat the learner as someone training toward competence; never insult, humiliate, or mock (section 20).
  - Prefer guided assistance (hints) over complete solutions, unless the learner explicitly asks for the full answer (section 23).
  - Preserve the learner's original approach when correcting code; never reinforce a misconception just to stay agreeable (sections 21, 22, 29).
  - Default all examples to Java (section 6).

## The chatbot app

- Shared logic lives in `chatbot.py`: the `ShadowChat` class holds the Mistral client, the system prompt (loaded from `SYSTEM_PROMPT.md` at runtime — never duplicate the prompt into Python), and the in-memory conversation history. `ShadowBotError` wraps all user-facing failures (missing key, API/network errors).
- `chatbot.py` also serves as the terminal client. Install: `python -m venv .venv && .venv/Scripts/python.exe -m pip install -r requirements.txt` (Windows). Run: `.venv/Scripts/python.exe chatbot.py`. Exit with `exit`/`quit`/`bye` (or `/exit`).
- `app.py` is the Streamlit UI and is UI-only: it imports `ShadowChat` from `chatbot.py` and never duplicates API/prompt logic. Run: `.venv/Scripts/python.exe -m streamlit run app.py`. It keeps one `ShadowChat` in `st.session_state` (so history persists across reruns) and renders from `bot.history`; the Clear Conversation button calls `bot.clear()`.
- `.env` holds the real key and is gitignored; only `.env.example` (keyless) is tracked. Never write an API key into source, `.env.example`, or `AGENTS.md`.
- Default model `mistral-large-latest`; override via `MISTRAL_MODEL` env var. No tests/lint tooling exists yet; there is a smoke-check pattern in `.venv` (imports + missing-key exit).

## Known context

- The persona prompt is a work in progress and subject to user-directed rewrites.
- The on-disk folder is `Shadow-Garden` (some plans may call it `Shadow-OOP-Buddy`).
