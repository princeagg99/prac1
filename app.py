import streamlit as st

def get_color_based_on_range(value):
    if value < 25:
        return "red"
    elif value < 50:
        return "orange"
    elif value < 75:
        return "yellow"
    else:
        return "green"

def main():
    st.title("Colored Icon/Button based on Number Range")
    
    # Get user input
    number_input = st.slider("Select a number:", min_value=0, max_value=100, value=50)
    
    # Get color based on number range
    color = get_color_based_on_range(number_input)
    
    # Add some padding and set button's style using CSS
    st.markdown(
        f"""
        <style>
        .button {{
            background-color: {color};
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
            margin-top: 20px;
        }}
        </style>
        """
        , unsafe_allow_html=True
    )
    
    # Display the button with the chosen color
    st.markdown(
        f'<button class="button">Number is {number_input}</button>',
        unsafe_allow_html=True
    )

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
