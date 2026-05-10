from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from core.database import Base


class AgentLog(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True, index=True)

    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)

    step = Column(String, nullable=False)  # intent, availability, negotiation, booking

    input = Column(JSON, nullable=True)
    output = Column(JSON, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    ticket = relationship("Ticket")