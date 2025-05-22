from sqlalchemy import Column, Integer, Text, Boolean, VARCHAR
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=False)
