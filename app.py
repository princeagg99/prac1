import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

# Create a sample dataframe
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 35, 40, 25],
    'Gender': ['Male', 'Female', 'Male', 'Female']
}
df = pd.DataFrame(data)

# Display the dataframe with editable parameter set to True
editable_df = st.dataframe(df, editable=True)

# Optionally, you can capture the edited dataframe
# if you want to do something with it later
# edited_data = editable_df.data

























# import streamlit as st



# def summarize_gpt(tmp_table_gpt):
#     st.markdown("""<span style="font-size: 24px; ">Summarize key findings of the case.</span>""", unsafe_allow_html=True)
#     st.write()
#     # Initialize session state
#     if 'show_second_button' not in st.session_state:
#         st.session_state.show_second_button = False

    
#     # First button
#     if st.button("Summarize"):
#         with st.spinner("Summarizing...."):
#             tab1=st.session_state["displaytable_gpt"]
#             summ_data = ', '.join(tab1['Answer']) + st.session_state["sara_recommendation_gpt"] 
#             response_summ_gpt = summ_gpt_(summ_data)
#             response_summ_gpt = response_summ_gpt.replace("$", " ")
#             st.session_state.summary_cs_fd = response_summ_gpt
#             st.write(response_summ_gpt)
#             st.session_state["tmp_summary_gpt"] = response_summ_gpt
#             st.markdown("#### Summarization Feedback:")
        
#         # Display the second button only if the first button is clicked
#         if st.session_state.show_second_button is None:
#             st.session_state.show_second_button = False
#         if not st.session_state.show_second_button:
#             st.session_state.show_second_button = True
#     # Second button
#     if st.session_state.show_second_button:
#         col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
#         with col_1:
#             if st.button("👍🏻"):
                
#                 st.write('Thanks! Your Feedback is recorded ')
#         with col_2:
#             if st.button("👎🏻"):
                
#                 st.write('Thanks! Your Feedback is recorded ')
        



# # Call the nested button function
# summarize_gpt()
