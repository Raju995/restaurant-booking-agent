from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from core.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))
    slot_id = Column(Integer, ForeignKey("slots.id"))

    status = Column(String, default="confirmed")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User")
    restaurant = relationship("Restaurant", back_populates="bookings")
    table = relationship("Table", back_populates="bookings")
    slot = relationship("Slot", back_populates="bookings")