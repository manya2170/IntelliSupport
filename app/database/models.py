
from sqlalchemy import Column, Integer, String, Text, DateTime, func

from app.database.database import Base


class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(100), nullable=False)

    email = Column(String(255), nullable=False)

    message = Column(Text, nullable=False)

    status = Column(String(20), default="open")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
