import streamlit as st
import importlib

st.title("My Engineering ML Projects Portfolio")
st.sidebar.title("Select a Project")

# Sidebar project selection
choice = st.sidebar.radio("Projects:", [
    "NNIT Student Support System",
    "Predictive Maintenance for Marine Engines",
    "Hull Biofouling Predictor and Optimizer",
    "User-Friendly Interactive Chatbot"
])

# Dictionary of project modules
projects = {
    "NNIT Student Support System": "nnit_students_chatbot",
    "Predictive Maintenance for Marine Engines": "predictive_maintenance_marine_engine",
    "Hull Biofouling Predictor and Optimizer": "hull_biofouling_prediction",
    "User-Friendly Interactive Chatbot": "user_interactive_chatbot"
}

# Placeholder container for dynamic project rendering
placeholder = st.empty()

# Dynamically load the selected project
module_name = projects[choice]

with placeholder:
    try:
        # Import the module
        module = importlib.import_module(module_name)
        # Reload to make sure changes or new selection runs
        importlib.reload(module)
    except Exception as e:
        st.error(f"Error loading project '{choice}': {e}")
