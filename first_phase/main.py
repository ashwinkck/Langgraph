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
graph_builder = StateGraph(State)
#Add a Node
graph_builder.add_node("greet",greet)
#Connect the graph
graph_builder.add_edge(START, "greet")
graph_builder.add_edge("greet",END)
# Compiling
graph = graph_builder.compile()
#Executing
result = graph.invoke(
    {
        "message":"Hello World!"
    }
)