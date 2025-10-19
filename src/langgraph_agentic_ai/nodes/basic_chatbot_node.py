from src.langgraph_agentic_ai.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot node implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state : State) -> dict:
        """
        Process the input state and generate a chabot response.
        """
        return {"message" : self.llm.invoke(state["message"])}