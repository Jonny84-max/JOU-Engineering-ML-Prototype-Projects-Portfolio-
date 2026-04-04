# app.py
import streamlit as st

st.title("My Engineering ML Projects Portfolio")
st.sidebar.title("Select a Project")

choice = st.sidebar.radio("Projects:", [
    "NNIT Student Support System",
    "Predictive Maintenance for Marine Engines",
    "Hull Biofouling Predictor and Optimizer",
    "User-Friendly Interactive Chatbot"
])

# Placeholder container
project_placeholder = st.empty()

# Dynamically load the project
if choice == "NNIT Student Support System":
    with project_placeholder:
        import nnit_students_chatbot  # This module runs top-level Streamlit code

elif choice == "Predictive Maintenance for Marine Engines":
    with project_placeholder:
        import predictive_maintenance_marine_engine

elif choice == "Hull Biofouling Predictor and Optimizer":
    with project_placeholder:
        import hull_biofouling_prediction

elif choice == "User-Friendly Interactive Chatbot":
    with project_placeholder:
        import user_interactive_chatbot
