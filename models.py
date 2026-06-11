from sqlalchemy import \
    Column, Integer, String, ForeignKey
from database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(String(280), nullable=False)

