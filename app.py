def summarize_gpt(tmp_table_gpt):
    st.markdown("""<span style="font-size: 24px; ">Summarize key findings of the case.</span>""", unsafe_allow_html=True)
    st.write() #This is to have gap between
    # Create a session state object
    session_state = st.session_state

    # Initialize session state variables
    if 'button_clicked' not in session_state:
        session_state.button_clicked = False

    # Create the first button
    if st.button("Summarize"):
        with st.spinner("Summarizing...."):
            st.write('Button 1 clicked')
            tab1=st.session_state["displaytable_gpt"]
            summ_data = ', '.join(tab1['Answer']) + st.session_state["sara_recommendation_gpt"] 
            response_summ_gpt = summ_gpt_(summ_data)
            response_summ_gpt = response_summ_gpt.replace("$", " ")
            response_summ_gpt = response_summ_gpt.replace("5,000", "5,000 USD")
            response_summ_gpt = response_summ_gpt.replace("5,600", "5,600 USD")
            st.session_state.summary_cs_fd = response_summ_gpt
            st.write(response_summ_gpt)
            st.session_state["tmp_summary_gpt"] = response_summ_gpt
            st.markdown("#### Summarization Feedback:")
            

    # Create the second button
    col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
    with col_1:
        if st.button("👍🏻"):
            # Set the session state variable to True when Button 2 is clicked
            session_state.button_clicked = True
    with col_2:
        if st.button("👎🏻"):
            # Set the session state variable to True when Button 2 is clicked
            session_state.button_clicked = True
    # Show a message if Button 2 has been clicked
    if session_state.button_clicked:
        st.write('Feedback is recorded!')
