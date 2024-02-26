import streamlit as st

def button_clicked(button_name):
   
    # Define the text for each button
    button_texts = {
        "Button 1": "This is the text for Button 1",
        "Button 2": "This is the text for Button 2",
        "Button 3": "This is the text for Button 3",
        "Button 4": "This is the text for Button 4",
        "Button 5": "This is the text for Button 5",
        "Button 6": "This is the text for Button 6"
    }
    
    # Create the buttons and associate each one with its respective text and click handler
    for button_name, text in button_texts.items():
        if st.button(button_name):
            button_clicked(button_name)
    
    # Create a space to display the output when a button is clicked
    st.write("\nOutput:")

button_clicked()













# import streamlit as st

# col1, col2, col3 = st.columns([6,3,6])

# with col1:
#     button1 = st.button('"What are the products that are associated with this customer?"')
#     if button1:
#         st.write("hello1")

# with col2:
#     button2 = st.button('"What asasaasre the products that are associated with this customer?"')
#     if button2:
#         st.write("hello2")
#         # Do something...

# with col3:
#     button3 = st.button("What asdascasv the products that are associated with this customer?")





# if button3:
#     st.write("hello3")
#     # Do something...









