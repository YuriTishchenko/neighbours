import enum

impport enum
from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.db.db import Base
from app.models.user_role import user_role


class SystemRole(enum.Enum):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    SUPERUSER = 'superuser'
    USER = 'user'
    NONE = 'none'

class User(Base):
    __tablename__ = "users"
    is_active = Column(Boolean, default=False)
    system_role = Column(
        Enum(SystemRole),
        default=SystemRole.NONE,
        nullable=False
    )
    roles = relationship(
        'Role',
        secondary=user_roles,
        backref='users'
    )
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    telegram_username = Column(String, nullable=True)
    flats = relationship("FlatUserLink", back_populates="user")
    surname = Column(String, nullable=True)

    @property
    def has_admin_rights(self) -> bool:
        return self.is_admin or self.is_superuser
    def has_role(self, role_name: str) -> bool:
        return any(role.name == role_name for role in self.roles)
