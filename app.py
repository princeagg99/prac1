import streamlit as st
import time

def print_with_spinner(output1, output2, output3):
    with st.spinner("Processing output 1..."):
        time.sleep(2)  # Simulating some processing time
        st.write(output1)

    with st.spinner("Processing output 2..."):
        time.sleep(2)  # Simulating some processing time
        st.write(output2)

    with st.spinner("Processing output 3..."):
        time.sleep(2)  # Simulating some processing time
        st.write(output3)

# Example usage
output1 = "This is output 1"
output2 = "This is output 2"
output3 = "This is output 3"

print_with_spinner(output1, output2, output3)
