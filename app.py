import streamlit as st

def button_action(button_name):
    return f"You clicked the {button_name} button!"

def main():
    st.title("Multiple Buttons Streamlit App")
    
    # Define dictionary to store button outputs
    button_outputs = {}

    # Define buttons
    buttons = ["Button 1", "Button 2", "Button 3"]

    # Iterate through buttons
    for button in buttons:
        # Check if button is clicked
        if st.button(button):
            # Store button output in dictionary
            button_outputs[button] = button_action(button)

    # Display outputs
    st.header("Button Outputs")
    for button, output in button_outputs.items():
        st.write(f"- {button}: {output}")

if __name__ == "__main__":
    main()















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









