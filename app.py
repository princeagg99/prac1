import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button('Button 1')
    if button1:
    st.write("hello1")

with col2:
    button2 = st.button('Button 2')

with col3:
    button3 = st.button('Button 3')



if button2:
    st.write("hello2")
    # Do something...

if button3:
    st.write("hello3")
    # Do something...
