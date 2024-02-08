import streamlit as st

# Create a placeholder to dynamically update content
output_placeholder = st.empty()

# Create a button
button_clicked = st.button("Click me!")

# Check if the button is clicked
if button_clicked:
    # Update the content of the placeholder without reloading the entire page
    output_placeholder.write("Button clicked!")
