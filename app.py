# import streamlit as st

# col1, col2, col3 = st.columns(3)

# with col1:
#     button1 = st.button('Button 1')
#     if button1:
#         st.write("hello1")

# with col2:
#     button2 = st.button('Button 2')
#     if button2:
#         st.write("hello2")
#         # Do something...

# with col3:
#     button3 = st.button('Button 3')





# if button3:
#     st.write("hello3")
#     # Do something...









import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
