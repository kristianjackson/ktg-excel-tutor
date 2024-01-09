# main.py
# Main application logic

import streamlit as st
import uuid
import io
from openai import OpenAI
import data_handling
import openai_interaction
import ui_components
import config


def initialize_session_state():
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())


def main():
    initialize_session_state()
    df = data_handling.handle_file_upload()
    if df is not None:
        json_str = data_handling.convert_df_to_json(df)
        ui_components.display_json_and_download_option(json_str)

    if "assistant" not in st.session_state:
        openai_interaction.initialize_openai_assistant()

    if "messages" in st.session_state:
        ui_components.display_chat_messages(st.session_state.messages)

    # Handle other Streamlit UI components as needed


if __name__ == "__main__":
    main()
