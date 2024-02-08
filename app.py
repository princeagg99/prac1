import streamlit as st

# Create a session state object
session_state = st.session_state

# Initialize session state variables for inner button
if 'inner_button_clicked' not in session_state:
    session_state.inner_button_clicked = False

# Outer button
if st.button('Outer Button'):
    st.write('Outer Button clicked')

    # Inner button
    if st.button('Inner Button'):
        session_state.inner_button_clicked = True

# Show a message if Inner Button has been clicked
if session_state.inner_button_clicked:
    st.write('Inner Button clicked')
