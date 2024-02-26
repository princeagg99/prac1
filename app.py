import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button('"What are the products that are associated with this customer?"')
    if button1:
        st.write("hello1")

with col2:
    button2 = st.button('Button 2')
    if button2:
        st.write("hello2")
        # Do something...

with col3:
    button3 = st.button('Button 3')





if button3:
    st.write("hello3")
    # Do something...









