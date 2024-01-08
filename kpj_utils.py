import streamlit as st


# Function to display session state data
def display_session_state_data():
    st.write("Current Session State Data:")
    for key, value in st.session_state.items():
        st.write(f"{key}: {value}")


# A sample input to demonstrate session state
if "count" not in st.session_state:
    st.session_state.count = 0

increment = st.button("Increment")
if increment:
    st.session_state.count += 1
