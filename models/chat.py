from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from core.database import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)

    sender = Column(String, nullable=False)  # "user" or "agent"
    message = Column(Text, nullable=False)

    agent_step = Column(String, nullable=True)  # intent, availability, negotiation, booking

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    ticket = relationship("Ticket")