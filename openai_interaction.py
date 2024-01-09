# openai_interaction.py
# Functions to interact with the OpenAI API

import streamlit as st
import openai

client = openai.OpenAI()


def initialize_openai_assistant():
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    st.session_state.assistant = openai.beta.assistants.retrieve(
        st.secrets["OPENAI_ASSISTANT"]
    )
    st.session_state.thread = client.beta.threads.create(
        metadata={"session_id": st.session_state.session_id}
    )
