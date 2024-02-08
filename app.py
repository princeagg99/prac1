import streamlit as st


def summarize_gpt():
    st.markdown("""<span style="font-size: 24px; ">Summarize key findings of the case.</span>""", unsafe_allow_html=True)
    st.write() #This is to have gap between
    
    button1 = st.button("Summarize")

    if st.session_state.get('button') != True:
    
        st.session_state['button'] = button1
    

    if st.session_state['button'] == True:
        with st.spinner("Summarizing...."):
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
            col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
            with col_1:
        
                if st.button("👍🏻"):
                    
            
                    st.write("Feedback is recorded!")
            
                    st.session_state['button'] = False
            with col_2:
        
                if st.button("👎🏻"):
                    
            
                    st.write("Feedback is recorded!")
            
                    st.session_state['button'] = False

summarize_gpt()

