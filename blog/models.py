from sqlalchemy import Column, BigInteger, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(
        BigInteger,
        primary_key=True,
        index=True
    )
    title = Column(
        String(255),
        nullable=False
    )
    body = Column(
        Text,
        nullable=False
    )
    user_id = Column(
        BigInteger,
        ForeignKey('users.id'),
        nullable=False
    )

    author = relationship("models.User", back_populates="blogs")
