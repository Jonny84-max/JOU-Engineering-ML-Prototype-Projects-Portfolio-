import streamlit as st
import nnit_Students_chatbot
import marine_maintenance
import hull_biofouling
import interactive_chatbot

st.title("My Engineering ML Projects Portfolio")
st.sidebar.title("Select a Project")

choice = st.sidebar.radio("Projects:", [
    "NNIT Student Support System",
    "Predictive Maintenance for Marine Engines",
    "Hull Biofouling Predictor and Optimizer",
    "User-Friendly Interactive Chatbot"
])

if choice == "NNIT Student Support System":
    nnit_chatbot.run()
elif choice == "Predictive Maintenance for Marine Engines":
    marine_maintenance.run()
elif choice == "Hull Biofouling Predictor and Optimizer":
    hull_biofouling.run()
elif choice == "User-Friendly Interactive Chatbot":
    interactive_chatbot.run()
