from sqlalchemy import Column, BigInteger, String, Text
from database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(
        BigInteger,
        primary_key=True,
        index=True
    )
    title = Column(
        String(255)
    )
    body = Column(
        Text
    )
