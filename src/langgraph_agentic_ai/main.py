import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamUI
from src.langgraph_agentic_ai.LLMs.groq_llm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder

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
    
    user_message = st.chat_input("Enetr your message : ")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input = user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error : LLM Model could not be initialized")
                return 

            usecase = user_input.get("selected_usecase")
        
            # Graph Builder

            graph_builder = GraphBuilder()

            try:
                graph = graph_builder.setup_graph(usecase)
            
            except Exception as e:
                st.error(f"Error : Graph set up failed - {e}")

        except Exception as e:
            st.error("")