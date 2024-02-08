import streamlit as st
def summarize_gpt():

    session_state = st.session_state

    if 's1' not in session_state:
        session_state.s1 = False
    if 's2' not in session_state:
        session_state.s2 = False

    st.markdown("""<span style="font-size: 24px; ">Summarize key findings of the case.</span>""", unsafe_allow_html=True)
    st.write() #This is to have gap between
    #summ_gpt = st.button("Summarize")
    if session_state.s1 == False:
        if st.button('Summarize'):
            with st.spinner("Summarizing...."):
        
                st.write("this is the summarization")
    
                st.markdown("#### Summarization Feedback:")
                col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
    
                if session_state.s1 == False:
                    with col_1:
                        if st.button("👍🏻",key=4):
                            
                            session_state.s2 = False
                             
    
    
                    with col_2:
                        if st.button("👎🏻",key=5):
                            
    
    
                            session_state.s2 = False
                           

    if session_state.s2 == False:
       st.write('Feedback is recorded!')
        
        
summarize_gpt()
