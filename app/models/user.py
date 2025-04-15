from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    telegram_username = Column(String, nullable=True)

    flats = relationship("FlatUserLink", back_populates="user")
