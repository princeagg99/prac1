import streamlit as st

# Define function to initialize session state
def init_session_state():
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False

# Initialize session state
init_session_state()

# Define function to handle button clicks
def handle_button_clicks():
    if st.button('Button 1'):
        st.write('Button 1 clicked!')
    if st.button('Button 2'):
        st.session_state.button_clicked = True

# Display buttons and handle clicks
handle_button_clicks()

# Show message if button 2 is clicked
if st.session_state.button_clicked:
    st.write('Button 2 clicked! This message will persist even after the page reloads.')
