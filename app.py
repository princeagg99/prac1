import streamlit as st


def summarize_gpt():
    st.markdown("""<span style="font-size: 24px; ">Summarize key findings of the case.</span>""", unsafe_allow_html=True)
    st.write() #This is to have gap between
    
    button1 = st.button("Summarize")

    if st.session_state.get('button') != True:
    
        st.session_state['button'] = button1
    

    if st.session_state['button'] == True:
        
    
        st.write("this is the summary")

        st.markdown("#### Summarization Feedback:")
    
        if st.button("👍🏻"):
            
    
            st.write("recorded")
    
            st.session_state['button'] = False

summarize_gpt()

