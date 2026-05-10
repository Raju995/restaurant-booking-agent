from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from core.database import Base


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    capacity = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    restaurant = relationship("Restaurant", back_populates="tables")
    slots = relationship("Slot", back_populates="table")
    bookings = relationship("Booking", back_populates="table")