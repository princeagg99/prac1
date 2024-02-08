import streamlit as st

button1 = st.button('summarize....')

if st.session_state.get('button') != True:

    st.session_state['button'] = button1

if st.session_state['button'] == True:

    st.write("this is the summary")

    if st.button('give your feedback'):

        st.write("recorded")

        st.session_state['button'] = False

        st.checkbox('Reload')
