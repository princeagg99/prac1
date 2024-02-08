import streamlit as st

# Create a session state object
session_state = st.session_state

# Initialize session state variables
if 'button_clicked' not in session_state:
    session_state.button_clicked = False

# Outer button
if st.button('Outer Button'):
    st.write('Outer Button clicked')

    # Inner button
    if st.button('Inner Button'):
        # Set the session state variable to True when Inner Button is clicked
        session_state.button_clicked = True

# Show a message if Inner Button has been clicked
if session_state.button_clicked:
    st.write('Inner Button clicked')
