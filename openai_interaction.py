# openai_interaction.py
# Functions to interact with the OpenAI API

import streamlit as st
from openai import OpenAI
import config

client = OpenAI()


def initialize_openai_assistant():
    openai.api_key = config.OPENAI_API_KEY
    st.session_state.assistant = openai.beta.assistants.retrieve(
        st.secrets["OPENAI_ASSISTANT"]
    )
    st.session_state.thread = client.beta.threads.create(
        metadata={"session_id": st.session_state.session_id}
    )