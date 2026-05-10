from sqlalchemy.orm import Session

# from services.booking_services import create_booking,extract_intent
from services.availability_service import get_available_slots
from schemas.chat import ChatRequest, ChatResponse
from core.database import get_db
from models.ticket import Ticket
from services.availability_service import create_ticket
from agents.graph import app


async def handle_chat(db: Session, request:ChatRequest):
    try:
        message = request.message.lower()
        ##check for ticket id
        if "ticket_id" in request.model_fields_set:
            # ticket_id = int(request.match_info["ticket_id"])
            ticket=db.query(Ticket).filter(Ticket.id == request.ticket_id).first()
            result=ticket.context
        else:
            ##we need to create ticket id
            ticket=create_ticket(db,request.user_id)
            result=None

            print()

            # ----------------------------
            # BUILD STATE
            # ----------------------------
        state = {
            "db": db,
            "user_input": request.message,
            "user_id": request.user_id,



            "context": ticket.context or {},

            "action": None,

            "params": {},

            "result": result,

            "response": None
        }

        # ----------------------------
        # RUN LANGGRAPH
        # ----------------------------
        result = await app.ainvoke(state)

        # ----------------------------
        # SAVE CHAT HISTORY
        # ----------------------------
        if ticket.messages is None:
            ticket.messages = []
        ticket.messages.append({
            "role": "user",
            "content": request.message
        })

        ticket.messages.append({
            "role": "assistant",
            "content": result["response"]
        })

        # ----------------------------
        # SAVE CONTEXT MEMORY
        # ----------------------------
        ticket.context = result["context"]
        # ticket.context["slot_id"]=result["result"]["slot_id"]


        db.commit()

        return {
            "reply": result["response"],
            "ticket_id": ticket.id
        }
    except Exception as e:
        return {
            "error": e,

        }




    # intent_data = extract_intent(request.message)

    # 🔹 Very basic intent detection (temporary)
    # if "book" in message:
    #     # Dummy values (later from agent)
    #     restaurant_id = 1
    #     table_id = 1
    #     slot_id = 1
    #
    #     booking, msg = create_booking(
    #         db,
    #         request.user_id,
    #         restaurant_id,
    #         table_id,
    #         slot_id
    #     )
    #
    #     return {"reply": msg}
    #
    # elif "available" in message:
    #     slots = get_available_slots(db, restaurant_id=1, date="2026-04-30")
    #
    #     return {"reply": f"{len(slots)} slots available"}
    #
    # return {"reply": "I didn’t understand"}