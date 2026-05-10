from sqlalchemy import Column, Integer, ForeignKey, Date, Time, Boolean
from sqlalchemy.orm import relationship

from core.database import Base


class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))

    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)

    is_available = Column(Boolean, default=True)

    # Relationships
    restaurant = relationship("Restaurant", back_populates="slots")
    table = relationship("Table", back_populates="slots")
    bookings = relationship("Booking", back_populates="slot")