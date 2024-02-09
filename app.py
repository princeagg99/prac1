import streamlit as st
import pandas as pd

# Create a function to render editable DataFrame
def render_editable_df():
    # Initialize DataFrame with some data
    data = {'Column 1': [1, 2, 3],
            'Column 2': [4, 5, 6],
            'Column 3': [7, 8, 9]}
    df = pd.DataFrame(data)

    # Display DataFrame
    st.write(df)

    # Allow users to edit DataFrame
    st.write("Edit DataFrame:")
    for index, row in df.iterrows():
        for col in df.columns:
            df.at[index, col] = st.number_input(f"Edit {col} for row {index+1}", value=row[col])

    # Display the updated DataFrame
    st.write("Updated DataFrame:")
    st.write(df)

# Main function to run the Streamlit app
def main():
    st.title("Editable DataFrame Example")
    render_editable_df()

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
