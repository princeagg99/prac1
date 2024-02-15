import streamlit as st

# Set the font size
font_size = 16

# Create a text area with specified font size
text = st.text_area("Enter text here", height=200, key="text_area", value="", help="Text area", font_size=font_size)
