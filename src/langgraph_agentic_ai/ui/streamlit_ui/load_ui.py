import streamlit as st
import os

from src.langgraph_agentic_ai.ui.uiconfigfile import Config

class LoadStreamUI:

    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title = "🤖 " + self.config.get_page_title(), layout = "wide")
        st.header("🤖 "  + self.config.get_page_title())

        # Side Bar
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # User Controls
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API_KEY", type = "password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please Enter your GROQ API KEY to proceed. Don't have? refer : https://console.groq.com/keys")
                
            # Use Case Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)

            if self.user_controls['selected_usecase'] == "Chatbot with Web":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY_API_KEY", type = 'password')

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please Enter your TAVILY API KEY to proceed. Don't have? refer : https://app.tavily.com/home ")

        return self.user_controls  
                