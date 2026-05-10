from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from core.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    status = Column(String, default="active")
    context = Column(JSON, nullable=True)
    messages=Column(JSON, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User")