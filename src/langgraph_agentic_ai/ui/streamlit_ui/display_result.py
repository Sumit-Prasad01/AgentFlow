import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json
import re
class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    

    def strip_thoughts(self, message_content: str) -> str:
    # Remove <think>...</think> block if it exists
        return re.sub(r"<think>.*?</think>", "", message_content, flags=re.DOTALL).strip()


    def display_result_on_ui(self):

        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            for event in graph.stream({"messages" : ("user", user_message)}):
                # print(event.values())
                for value in event.values():
                    # print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        clean_message = self.strip_thoughts(value["messages"].content)
                        st.write(clean_message)