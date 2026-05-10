from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import SessionLocal
from schemas.chat import ChatRequest, ChatResponse
from services.chat_service import handle_chat

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    response = await handle_chat(db, request)

    return ChatResponse(
        reply=response["reply"],
        ticket_id=request.ticket_id or response["ticket_id"]
    )