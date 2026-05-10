from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    user_id: int
    message: str
    ticket_id: Optional[int] = None


class ChatResponse(BaseModel):
    reply: str
    ticket_id: int