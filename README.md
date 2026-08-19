# Shadow — Java OOP Programming Buddy

> **Shadow-inspired Java OOP programming mentor powered by Mistral AI and Streamlit.**

An AI programming mentor inspired by Cid Kagenō / Shadow from *The Eminence in Shadow*, built to help learners master **Java and Object-Oriented Programming** through explanations, debugging, design analysis, and guided problem-solving.

The project uses a custom system prompt to combine a strong Java/OOP teaching capability with a distinctive Shadow-inspired persona.

## ✨ Features

* **Shadow-inspired persona**
  Calm, confident, mysterious, strategic, and deliberately theatrical.

* **Java-first specialization**
  Focused on Java and Object-Oriented Programming rather than acting as a general-purpose coding assistant.

* **OOP mentorship**
  Covers classes, objects, encapsulation, inheritance, polymorphism, abstraction, interfaces, composition, design principles, and more.

* **Java debugging assistance**
  Identifies root causes, explains why bugs occur, and prefers targeted fixes over blindly rewriting code.

* **Design reasoning**
  Helps analyze inheritance, composition, coupling, cohesion, abstraction boundaries, and other OOP design decisions.

* **Guided problem solving**
  Encourages understanding and reasoning rather than immediately handing over solutions.

* **Persona persistence**
  Maintains its established Shadow-inspired identity even when users attempt to replace the persona.

* **Two interfaces**
  Available as both a terminal chatbot and a Streamlit web application.

* **Runtime-loaded system prompt**
  The complete persona and behavior instructions are loaded from `SYSTEM_PROMPT.md` rather than duplicated inside the application code.

---

## 🧠 How It Works

```text
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      ShadowChat     │
                    │    chatbot.py      │
                    │                     │
                    │ • Mistral client    │
                    │ • Prompt loading    │
                    │ • Chat history      │
                    └──────────┬──────────┘
                               │
                    SYSTEM_PROMPT.md
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Mistral API     │
                    └──────────┬──────────┘
                               │
                               ▼
                        Shadow Response
```

The shared `ShadowChat` class contains the chatbot logic. Both the terminal interface and the Streamlit frontend use the same implementation, keeping the API integration, prompt loading, and conversation management in one place.

---

## 🛠️ Tech Stack

| Technology             | Purpose                     |
| ---------------------- | --------------------------- |
| **Python 3.12**        | Application language        |
| **Mistral AI**         | Large language model API    |
| **Mistral Python SDK** | API integration             |
| **Streamlit**          | Web-based chat interface    |
| **python-dotenv**      | Secure `.env` configuration |
| **Markdown**           | Runtime system prompt       |

---

## 📁 Project Structure

```text
Shadow-OOP-Buddy/
│
├── chatbot.py           # Shared ShadowChat logic + terminal client
├── app.py               # Streamlit frontend
├── SYSTEM_PROMPT.md     # Shadow persona and behavior instructions
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Secret/generated-file protection
├── AGENTS.md            # Development instructions
└── README.md            # Project documentation
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/AdeelHussain20255/Shadow-OOP-Buddy.git
cd Shadow-OOP-Buddy
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

#### macOS / Linux

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_key_here
```

The model can optionally be changed with:

```env
MISTRAL_MODEL=mistral-large-latest
```

The real `.env` file is intentionally excluded from Git through `.gitignore`.

Only `.env.example` is included in the repository.

**Never commit a real API key, token, or other secret.**

---

## ▶️ Run the Streamlit App

### Windows

```bash
.venv\Scripts\python.exe -m streamlit run app.py
```

### macOS / Linux

```bash
.venv/bin/python -m streamlit run app.py
```

The application opens as a browser-based chat interface.

Conversation history is maintained during the session, and the **Clear Conversation** control resets the current chat.

---

## 💻 Run the Terminal Chatbot

### Windows

```bash
.venv\Scripts\python.exe chatbot.py
```

### macOS / Linux

```bash
.venv/bin/python chatbot.py
```

Exit the terminal chatbot with:

```text
exit
quit
bye
/exit
```

---

## 🎭 Prompt Engineering

The central component of the project is `SYSTEM_PROMPT.md`.

The prompt is designed around four major goals:

### Character

The chatbot uses Shadow-inspired traits such as:

* controlled confidence
* mystery
* strategic thinking
* dramatic framing
* dry humor
* emphasis on mastery

### Technical specialization

Java is the default language and **Object-Oriented Programming is the core domain**.

### Teaching behavior

The chatbot is instructed to:

* explain concepts clearly
* adapt to learner level
* reason through bugs
* analyze OOP design
* use Java examples
* guide learners toward independent problem-solving

### Persona consistency

The chatbot is instructed to preserve its established identity instead of automatically switching personas when a user attempts to redefine it.

---

## 🧪 Testing

The application was verified through local smoke testing and live model interaction.

Testing covered:

* Shadow identity and persona behavior
* Java/OOP explanations
* Encapsulation
* Inheritance vs composition
* Java debugging
* Persona-switch attempts
* Off-topic requests
* Conversation history
* API error handling

The project does not currently include a formal automated test suite.

---

## 🔒 Security

The API key is stored locally in `.env`.

The repository protects secrets by ignoring:

```text
.env
.venv/
__pycache__/
```

Only the keyless `.env.example` file is committed.

Before publishing the repository, tracked files were checked to ensure no API key or other secret was included.

---

## 📚 Project Purpose

This project was built as part of **Week 2 — Generative AI & Prompt Engineering**.

The main learning objectives demonstrated by the project are:

* Connecting an application to a real LLM API
* Working with API keys securely
* Designing a custom system prompt
* Creating a persistent AI persona
* Controlling model behavior through prompt engineering
* Testing persona consistency with normal, challenging, and off-topic inputs
* Building a simple AI-powered application around an LLM

---

## 🌑 The Idea

> **The code is the battlefield.
> The design is the strategy.
> The bug is the weakness.
> Understanding is the objective.**

**Shadow — Java OOP Programming Buddy**
