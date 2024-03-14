import streamlit as st
import time
import threading

def print_with_spinner(output, spinner_text):
    with st.spinner(spinner_text):
        time.sleep(2)  # Simulating some processing time
        st.write(output)

# Example usage
output1 = "This is output 1"
output2 = "This is output 2"
output3 = "This is output 3"

# Create and start a thread for each spinner-output pair
thread1 = threading.Thread(target=print_with_spinner, args=(output1, "Processing output 1..."))
thread2 = threading.Thread(target=print_with_spinner, args=(output2, "Processing output 2..."))
thread3 = threading.Thread(target=print_with_spinner, args=(output3, "Processing output 3..."))

thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()
