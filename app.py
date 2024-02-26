import streamlit as st

col1, col2, col3 = st.columns([6,3,2])

with col1:
    button1 = st.button('"What are the products that are associated with this customer?"')
    if button1:
        st.write("hello1")

with col2:
    button2 = st.button('"What asasaasre the products that are associated with this customer?"')
    if button2:
        st.write("hello2")
        # Do something...

with col3:
    button3 = st.button("What asdascasv the products that are associated with this customer?")





if button3:
    st.write("hello3")
    # Do something...









