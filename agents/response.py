async def response_node(state):

    action = state["action"]

    result = state["result"]

    if action == "check_availability":

        if result.get("available"):

            state["response"] = (
                f"Yes, table available at "
                f"{state['params']['time']} "
                f"for {state['params']['people']} people."
            )

        else:

            state["response"] = "Sorry, table unavailable."

    elif action == "create_booking":

        state["response"] = "✅ Booking confirmed."

    else:

        state["response"] = "Done."

    return state