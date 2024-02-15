import streamlit as st
st.session_state.user_summary = "abcd"
#st.text_area("**Update the system generated summary**", st.session_state.user_summary, height = 300, help = "Once the system summarizes the key findings of the case, you can edit it as per your consideration. After downloading the report, the user summary is reset.", placeholder = "Press Summarize button above to summarize the key findings of the case.")

st.text_area("**Update the system generated summary**", st.session_state.user_summary, height = 300, help = "Once the system summarizes the key findings of the case, you can edit it as per your consideration. After downloading the report, the user summary is reset.", placeholder = "Press Summarize button above to summarize the key findings of the case.")
