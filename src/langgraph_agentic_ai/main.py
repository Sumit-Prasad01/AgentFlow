import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamUI



def load_langgraph_agentic_ai_app():

    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    """

    # load UI

    ui = LoadStreamUI()
    user_input = ui.load_streamlit_ui()


    if not user_input:
        st.error("Error : Failed to load imput from the UI.")
        return 
    
    usre_message = st.chat_input("Enetr your message : ")

    # if usre_message:
    #     try:
    #         # Configure LLM
    #         obg_llm_config = GroqLLM(user_controls_input = user_input)
    #         model = obg_llm_config.get_llm_model()