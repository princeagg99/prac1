import streamlit as st

# Create a session state object
session_state = st.session_state

# Initialize session state variables
if 'button_clicked' not in session_state:
    session_state.button_clicked = False

# Create the first button
if st.button('Button 1'):
    st.write('Button 1 clicked')

# Create the second button
if st.button('Button 2'):
    # Set the session state variable to True when Button 2 is clicked
    session_state.button_clicked = True

# Show a message if Button 2 has been clicked
if session_state.button_clicked:
    st.write('Button 2 clicked')
