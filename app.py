import streamlit as st

# Initialize session state
if 'show_second_button' not in st.session_state:
    st.session_state.show_second_button = False

def summarize_gpt():
    # First button
    if st.button("button1"):
        st.write("first button clicked!")
        # Display the second button only if the first button is clicked
        if st.session_state.show_second_button is None:
            st.session_state.show_second_button = False
        if not st.session_state.show_second_button:
            st.session_state.show_second_button = True
    # Second button
    if st.session_state.show_second_button:
        # This button won't reload the page
        if st.button("button 2"):
            st.write("Second button clicked!")



# Call the nested button function
summarize_gpt()
