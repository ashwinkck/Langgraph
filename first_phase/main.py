from typing import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph import START, END


class State(TypedDict):
    message: str
def greet(state: State):
    print("Greating Node Executed")

    return {
        "message": state["message"] + "Welcome to LangGraph!"
        }
# Create the Graph
