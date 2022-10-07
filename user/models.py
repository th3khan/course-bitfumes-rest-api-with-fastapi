from sqlalchemy import Column, BigInteger, String
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(
        BigInteger,
        primary_key=True,
        index=True
    )
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
