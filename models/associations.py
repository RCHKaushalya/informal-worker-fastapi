from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db import Base

user_skills = Table(
    "user_skills",
    Base.metadata,
    Column("nic", String, ForeignKey("users.nic"), primary_key=True),
    Column("skill_id", Integer, ForeignKey("skills.id"), primary_key=True),
)