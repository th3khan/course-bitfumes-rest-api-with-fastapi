from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
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

    blogs = relationship('models.Blog', back_populates="author")
