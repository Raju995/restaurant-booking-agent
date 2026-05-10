from langgraph.graph import StateGraph, END

from agents.state import AgentState

from agents.intent import intent_node
from agents.tool_call import tool_node
from agents.response import response_node


graph = StateGraph(AgentState)

# add nodes
graph.add_node("intent", intent_node)

graph.add_node("tool", tool_node)

graph.add_node("response", response_node)

# start point
graph.set_entry_point("intent")

# flow
graph.add_edge("intent", "tool")

graph.add_edge("tool", "response")

graph.add_edge("response", END)

# compile
app = graph.compile()