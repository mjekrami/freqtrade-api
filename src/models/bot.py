from .base import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, func


class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    name = Column(String(32), nullable=False)
    is_running = Column(Boolean, default=False)
    creation_date = Column(DateTime, default=func.now())
