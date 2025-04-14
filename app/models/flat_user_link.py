from enum import Enum
from sqlalchemy import Column, Integer, ForeignKey, Enum as SQLAEnum
from sqlalchemy.orm import relationship
from app.db.base import Base

class UserFlatRole(str, Enum):
    OWNER = "owner"
    RENTER = "renter"

class FlatUserLink(Base):
    __tablename__ = "flat_user_link"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flat_id = Column(Integer, ForeignKey("flats.id"))
    role = Column(SQLAEnum(UserFlatRole), nullable=False)

    user = relationship("User", back_populates="flats")
    flat = relationship("Flat", back_populates="users")
