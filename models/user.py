from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from .associations import user_skills

class User(Base):
    __tablename__ = "users"

    nic = Column(String, primary_key=True, index=True, unique=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    language = Column(String, nullable=False)

    profile_image = Column(String, nullable=True, default='')
    district = Column(String, default='', nullable=True)
    ds = Column(String, default='', nullable=True)

    skills = relationship("Skill", secondary=user_skills, back_populates="users")