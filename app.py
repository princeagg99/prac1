def summarize_gpt(tmp_table_gpt):

    
    if 'summary_genenrated' not in st.session_state:
        st.session_state.summary_genenrated = False
    
    # def set_clicked2():
    #     st.session_state.clicked2 = True
    #     st.session_state.disabled = True

    st.markdown("""<span style="font-size: 24px; ">Summarize key findings of the case.</span>""", unsafe_allow_html=True)
    st.write() #This is to have gap between
    if st.session_state.summary_genenrated  == False:
        with st.spinner("Summarizing...."):
            summ_gpt = st.button("Summarize")
            if summ_gpt:
                tab1=st.session_state["displaytable_gpt"]
                summ_data = ', '.join(tab1['Answer']) + st.session_state["sara_recommendation_gpt"] 
                response_summ_gpt = summ_gpt_(summ_data)
                response_summ_gpt = response_summ_gpt.replace("$", " ")
                response_summ_gpt = response_summ_gpt.replace("5,000", "5,000 USD")
                response_summ_gpt = response_summ_gpt.replace("5,600", "5,600 USD")
                st.session_state.summary_cs_fd = response_summ_gpt
                st.write(response_summ_gpt)
                st.write("1234")


                st.session_state["tmp_summary_gpt"] = response_summ_gpt
                st.markdown("#### Summarization Feedback:")
                col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)

                with col_1:
                    if st.button("👍🏻",key=4):
                        
                        st.write("*Feedback is recorded*")
                        # st.session_state.summary_genenrated = True


                with col_2:
                    if st.button("👎🏻",key=5):
                        


                        st.write("*Feedback is recorded*")
                        # st.session_state.summary_genenrated = True

            else:
                st.write(st.session_state["tmp_summary_gpt"])
                st.write("*Thank you, your feedback is recorded*") 




   
 
    
       
            
            
    
           
            

                   

    return st.session_state["tmp_summary_gpt"] 
