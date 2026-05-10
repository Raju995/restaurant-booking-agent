from agents.tools import TOOLS


async def tool_node(state):

    action = state["action"]

    tool = TOOLS.get(action)

    if not tool:

        state["result"] = {
            "error": "Tool not found"
        }

        return state

    kwargs = {
        "db": state["db"],
        **state["params"]
    }

    # extra params for specific tool
    if action == "create_booking":
        kwargs["user_id"]=state["user_id"]

        kwargs["slot_id"] = state["context"]["slot_id"]

    result = await tool(**kwargs)

    state["result"] = result

    # 🔥 Save booking context
    if action == "check_availability":

        if result.get("available"):

            state["context"] = state["params"]
            state["context"]["slot_id"] = result["slot_id"]

    return state