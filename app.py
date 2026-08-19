"""Shadow OOP Programming Buddy - Streamlit frontend.

UI only: the Mistral API integration, system prompt loading, and
conversation history live in chatbot.ShadowChat.
"""

import streamlit as st

from chatbot import ShadowBotError, ShadowChat

EMPTY_SYSTEM_ROLES = {"system"}


def render_history(history: list[dict]) -> None:
    for message in history:
        if message["role"] in EMPTY_SYSTEM_ROLES:
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def main() -> None:
    st.set_page_config(
        page_title="Shadow - OOP Programming Buddy",
        page_icon="🌑",
        layout="centered",
    )

    st.title("Shadow - OOP Programming Buddy")
    st.caption("An AI programming mentor inspired by The Eminence in Shadow.")

    if "bot" not in st.session_state:
        try:
            st.session_state.bot = ShadowChat()
        except ShadowBotError as exc:
            st.error(str(exc))
            st.stop()

    bot: ShadowChat = st.session_state.bot

    if st.button("Clear Conversation"):
        bot.clear()
        st.rerun()

    render_history(bot.history)

    prompt = st.chat_input("Ask Shadow about OOP...")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Shadow contemplates your question..."):
                try:
                    content = bot.send_message(prompt)
                except ShadowBotError as exc:
                    st.error(str(exc))
                else:
                    st.markdown(content)


if __name__ == "__main__":
    main()