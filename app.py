import streamlit as st
import pandas as pd

# Function to create an editable DataFrame
def create_editable_df():
    # Create a sample DataFrame
    data = {
        'Name': ['John', 'Alice', 'Bob'],
        'Age': [30, 25, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    
    # Create an empty DataFrame to hold the edited values
    edited_df = pd.DataFrame(columns=df.columns)
    
    # Display the DataFrame and allow editing
    editable_df = st.table(df)
    
    # Loop through the rows of the original DataFrame
    for i, row in enumerate(df.itertuples(index=False)):
        # Create an empty dictionary to hold the edited values for this row
        edited_row = {}
        # Loop through each column
        for j, col in enumerate(df.columns):
            # Get the edited value from the user input
            edited_value = st.text_input(f"Edit {col} for row {i+1}", row[j])
            # Add the edited value to the dictionary
            edited_row[col] = edited_value
        # Append the edited row to the edited DataFrame
        edited_df = edited_df.append(edited_row, ignore_index=True)
    
    return edited_df

# Main function
def main():
    st.title("Editable DataFrame in Streamlit")
    
    # Create an editable DataFrame
    edited_df = create_editable_df()
    
    # Display the edited DataFrame
    st.write("Edited DataFrame:", edited_df)

if __name__ == "__main__":
    main()























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
