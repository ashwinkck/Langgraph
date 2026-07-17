from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# -----------------------------
# Shared State
# -----------------------------
class State(TypedDict):
    number: int


# -----------------------------
# Router Node
# -----------------------------
def router(state: State):
    print(f"Received Number: {state['number']}")
    return state


# -----------------------------
# Large Number Node
# -----------------------------
def large_number(state: State):
    print("Large Number Node Executed")
    return state


# -----------------------------
# Small Number Node
# -----------------------------
def small_number(state: State):
    print("Small Number Node Executed")
    return state


# -----------------------------
# Routing Function
# -----------------------------
def decide_route(state: State):

    if state["number"] > 10:
        return "large"

    return "small"


# -----------------------------
# Build Graph
# -----------------------------
graph_builder = StateGraph(State)

graph_builder.add_node("router", router)
graph_builder.add_node("large", large_number)
graph_builder.add_node("small", small_number)

graph_builder.add_edge(START, "router")

graph_builder.add_conditional_edges(
    "router",
    decide_route,
    {
        "large": "large",
        "small": "small",
    },
)

graph_builder.add_edge("large", END)
graph_builder.add_edge("small", END)

graph = graph_builder.compile()


# -----------------------------
# Run Graph
# -----------------------------
result = graph.invoke(
    {
        "number": 15
    }
)

print(result)