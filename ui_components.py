# ui_components.py
# Functions for different UI components

import streamlit as st


def display_chat_messages(messages):
    for message in reversed(messages):
        if message.role in ["user", "assistant"]:
            with st.chat_message(message.role):
                st.markdown(message.content)


def display_json_and_download_option(json_str):
    st.text_area("JSON Output", json_str, height=300)
    st.download_button(
        label="Download JSON",
        data=json_str,
        file_name="data.json",
        mime="application/json",
    )
