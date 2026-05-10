from services.booking_services import decide_action


async def intent_node(state):

    decision = await decide_action(state)

    params = decision.get("parameters", {})

    # 🔥 merge old context
    old_context = state["context"]

    merged_params = {
        "date": params.get("date") or old_context.get("date"),
        "time": params.get("time") or old_context.get("time"),
        "people": params.get("people") or old_context.get("people"),
    }

    state["action"] = decision["action"]

    state["params"] = merged_params

    return state