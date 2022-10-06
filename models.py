from sqlalchemy import Column, Integer, String, Table, ForeignKey, CheckConstraint, Text, Float, DateTime, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from database import Base

class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(20), unique=False)
    author = Column(String(20), unique=False)
    price = Column(Integer, unique=False)
    pages = Column(String(20), unique=False)





