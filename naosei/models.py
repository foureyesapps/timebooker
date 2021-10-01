from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cellphone = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
