"""Shadow OOP Programming Buddy - shared chat logic + terminal client.

The terminal client and the Streamlit frontend (app.py) both use the
ShadowChat class defined here, so the Mistral API integration and the
system prompt live in exactly one place.
"""

import os
import sys
from pathlib import Path

import httpx
from dotenv import load_dotenv
from mistralai.client import Mistral
from mistralai.client.errors.mistralerror import MistralError

PROMPT_FILE = Path(__file__).resolve().parent / "SYSTEM_PROMPT.md"
MODEL = os.getenv("MISTRAL_MODEL", "mistral-large-latest")
EXIT_COMMANDS = {"exit", "quit", "bye", "/exit", "/quit", "/bye"}


class ShadowBotError(Exception):
    """User-facing error: missing key, unreadable prompt, or failed API call."""


def load_system_prompt() -> str:
    try:
        return PROMPT_FILE.read_text(encoding="utf-8").strip()
    except OSError as exc:
        raise ShadowBotError(f"Could not read the system prompt file: {exc}")


def get_api_key() -> str:
    key = os.getenv("MISTRAL_API_KEY", "").strip()
    if not key:
        raise ShadowBotError(
            "MISTRAL_API_KEY is not set. Copy .env.example to .env, add your key, then run again."
        )
    return key


class ShadowChat:
    """Holds the Mistral client, the system prompt, and the conversation history."""

    def __init__(self, api_key: str | None = None, model: str | None = None) -> None:
        load_dotenv()
        self._api_key = api_key or get_api_key()
        self._model = model or MODEL
        self.system_prompt = load_system_prompt()
        self._client = Mistral(api_key=self._api_key)
        self.history = [{"role": "system", "content": self.system_prompt}]

    def send_message(self, user_text: str) -> str:
        self.history.append({"role": "user", "content": user_text})
        try:
            response = self._client.chat.complete(model=self._model, messages=self.history)
        except MistralError as exc:
            self.history.pop()
            raise ShadowBotError(f"Mistral API: {exc}") from exc
        except httpx.HTTPError as exc:
            self.history.pop()
            raise ShadowBotError(f"Network problem: {exc}") from exc
        except Exception as exc:
            self.history.pop()
            raise ShadowBotError(f"Unexpected error: {exc}") from exc

        if not response.choices or not response.choices[0].message.content:
            self.history.pop()
            raise ShadowBotError("The model returned an empty response.")

        content = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": content})
        return content

    def clear(self) -> None:
        self.history = [{"role": "system", "content": self.system_prompt}]


def main() -> None:
    load_dotenv()
    try:
        bot = ShadowChat()
    except ShadowBotError as exc:
        print(f"[error] {exc}")
        sys.exit(1)

    print()
    print("Shadow OOP Programming Buddy")
    print("Type 'exit' or '/quit' to leave.")
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            print("Shadow: The path ends here. Farewell.")
            break

        if not user_input:
            continue
        if user_input.lower() in EXIT_COMMANDS:
            print("Shadow: Farewell. May your code remain clean.")
            break

        try:
            content = bot.send_message(user_input)
        except ShadowBotError as exc:
            print(f"[error] {exc}")
            continue

        print()
        print(f"Shadow: {content}")
        print()


if __name__ == "__main__":
    main()