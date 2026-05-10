from sqlalchemy.orm import Session
from models.booking import Booking
from models.slot import Slot
from core.llm import call_ollama
import json
import os


async def create_booking(
    db: Session,
    user_id: int,


    slot_id: int,**kwargs
):
    resturant_id=1
    # 🔒 Check if slot is available
    slot = db.query(Slot).filter(Slot.id == slot_id).first()

    if not slot or not slot.is_available:
        return None, "Slot not available"

    # ✅ Create booking
    booking = Booking(
        user_id=user_id,
        restaurant_id=resturant_id,
        table_id=slot.table.id,
        slot_id=slot_id,
        status="confirmed"
    )

    # ❗ Mark slot unavailable
    slot.is_available = False

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking, "Booking confirmed"
import json
from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

# OpenRouter configuration
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",   # OpenRouter model name
    temperature=0,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

prompt = ChatPromptTemplate.from_template("""
You are a restaurant booking AI assistant.



Booking Context:
{context}

User Message:
{input}

Available actions:
- check_availability
- create_booking

Rules:
- If user asks availability -> check_availability
- If user says "book it" -> create_booking using previous contex
- For the year please consider current year 2026

Return ONLY valid JSON.

Example:
{{
    "action": "check_availability",
    "parameters": {{
        "date": "2026-05-08",
        "time": "20:30",
        "people": 4
    }}
}}
""")


async def decide_action(state):

    chain = prompt | llm

    response = await chain.ainvoke({

        "context": state["context"],
        "input": state["user_input"]
    })

    return json.loads(response.content)
# def extract_intent(message):
#     try:
#         prompt = f"""
#         You are an AI assistant for restaurant booking.
#
#         Extract structured data from the message.
#
#         Return ONLY valid JSON.
#
#         Message: "{message}"
#
#         JSON format:
#         {{
#           "intent": "booking | availability | unknown",
#           "restaurant_id": int or null,
#           "date": "YYYY-MM-DD" or null,
#           "time": "HH:MM" or null,
#           "people": int or null
#         }}
#         """
#
#         raw_output = call_ollama(prompt)
#
#         try:
#             return json.loads(raw_output)
#         except:
#             return {"intent": "unknown"}
#     except Exception as e:
#         print(e)