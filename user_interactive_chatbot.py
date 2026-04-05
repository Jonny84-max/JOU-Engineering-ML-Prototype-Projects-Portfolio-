import datetime  # to get current date and time
import streamlit as st  # to create the chatbot interface
import gradio as gr     # gradio interface  

# Common title and description
Title_ = "Python_Chatbot"
Description_ = "A simple chatbot that greets you and shows the current date and time in WAT."

# Chatbot logic
def Python_Chatbot(name):
    wat = datetime.timezone(datetime.timedelta(hours=1))  # WAT timezone
    now = datetime.datetime.now(wat)  # current time in WAT
    date = now.strftime('%B %d, %Y')
    time = now.strftime('%I:%M %p')
    return f"Nice to meet you, {name}! Today's date is {date} and the current time in WAT is {time}."

# Streamlit interface
def run_streamlit():
    st.title(Title_)
    st.text(Description_)  # show description
    name = st.text_input("Hello! What is your name?")  # user input
    if name:
        response = Python_Chatbot(name)  # generate response
        st.text(response)  # show chatbot reply

# Gradio interface
def run_gradio():
    iface = gr.Interface(
        fn=Python_Chatbot,  # fixed the function name
        inputs=gr.Textbox(label="Hello! What is your name?"),
        outputs=gr.Textbox(label="Response"),
        title="Python_Chatbot (Gradio)",
        description=Description_  # reuse description
    )
    iface.launch()

# Platform selection and execution
platform = "streamlit"  # change to "gradio" to run Gradio
if platform.lower() == "gradio":
    user_interaction_chatbot.run_gradio()
elif platform.lower() == "streamlit":
    user_interaction_chatbot.run_streamlit()  # <-- THIS CALL ACTUALLY RUNS THE STREAMLIT APP
else:
    print("Unknown platform! Choose 'gradio' or 'streamlit'.")
