
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "events"

    event_id: Mapped[str] = mapped_column(String, primary_key=True)
    payment_id: Mapped[str] = mapped_column(String)
    merchant_id: Mapped[str] = mapped_column(String)
    customer_id: Mapped[str] = mapped_column(String)
    event_type: Mapped[str] = mapped_column(String)
    amount_minor: Mapped[int] = mapped_column(BigInteger)
    currency: Mapped[str] = mapped_column(String(3))
    event_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    received_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
