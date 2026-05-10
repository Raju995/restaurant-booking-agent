from sqlalchemy.orm import Session
from models.slot import Slot
from models.ticket import Ticket
from datetime import datetime


async def get_available_slots(db: Session, date,time,people,**kwargs):
    time_obj = datetime.strptime(time, "%H:%M").time()
    slot_available=db.query(Slot).filter(
        Slot.restaurant_id == 1,
        Slot.date == date,
        Slot.time == time_obj,
        Slot.is_available == True
    ).all()

    return {
        "available": True if slot_available else False,
        "slot_id":  slot_available[0].id
    }
def create_ticket(db:Session, user_id:int):
    try:
        ticket = Ticket(user_id=user_id, status="Open")
        db.add(ticket)
        db.commit()  # DB generates the ID here
        db.refresh(ticket)
        return ticket
    except Exception as e:
        print(e)
        return False