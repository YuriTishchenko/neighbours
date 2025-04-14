from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Flat(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    entrance = Column(String, nullable=True)
    floor = Column(Integer, nullable=True)
    square_meters = Column(Integer, nullable=True)

    users = relationship("FlatUserLink", back_populates="flat")