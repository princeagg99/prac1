def summarize_gpt():

    
    if 'summary_genenrated' not in st.session_state:
        st.session_state.summary_genenrated = True
    
    # def set_clicked2():
    #     st.session_state.clicked2 = True
    #     st.session_state.disabled = True

    st.markdown("""<span style="font-size: 24px; ">Summarize key findings of the case.</span>""", unsafe_allow_html=True)
    st.write() #This is to have gap between
    summ_gpt = st.button("Summarize")
    if summ_gpt:
        with st.spinner("Summarizing...."):
            st.session_state.summary_genenrated = True
            st.write("abcdefgh")
            st.write("1234")
            
            st.markdown("#### Summarization Feedback:")
            col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)

            with col_1:
                if st.button("👍🏻",key=4):
                    
                    st.session_state.summary_genenrated = False
                    st.write("*Feedback is recorded*")
                    # st.session_state.summary_genenrated = True


            with col_2:
                if st.button("👎🏻",key=5):
                    


                    st.write("*Feedback is recorded*")
                    # st.session_state.summary_genenrated = True

    elif st.session_state.summary_genenrated == False:
            st.write("*Thank you, your feedback is recorded*") 


                   



