import streamlit as st
import pandas as pd

# Function to parse user input and convert it into a dataframe
def parse_input_to_dataframe(input_text):
    # Split the input text by newline characters
    rows = input_text.split('\n')
    # Split each row by commas to get the values
    data = [row.split(',') for row in rows]
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    return df

# Display a textarea for user input
input_text = st.text_area("Enter data (comma-separated values, one row per line):")

# Parse the user input and display the dataframe
if input_text:
    df = parse_input_to_dataframe(input_text)
    st.dataframe(df)


























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
