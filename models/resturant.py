from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from core.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    tables = relationship("Table", back_populates="restaurant")
    slots = relationship("Slot", back_populates="restaurant")
    bookings = relationship("Booking", back_populates="restaurant")