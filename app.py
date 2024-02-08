import streamlit as st

def nested_button_function():
    # First button
    if st.button("Click me to show the second button"):
        # Display the second button only if the first button is clicked
        if st.session_state.show_second_button is None:
            st.session_state.show_second_button = False
        if not st.session_state.show_second_button:
            st.session_state.show_second_button = True
    # Second button
    if st.session_state.show_second_button:
        # This button won't reload the page
        if st.button("Second Button (No Page Reload)"):
            st.write("Second button clicked!")

# Initialize session state
if 'show_second_button' not in st.session_state:
    st.session_state.show_second_button = False

# Call the nested button function
nested_button_function()
