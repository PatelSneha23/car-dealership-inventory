from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Text,
    ForeignKey,
    TIMESTAMP,
    CheckConstraint
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(Text, nullable=False)

    role = Column(String(20), nullable=False, default="USER")

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )

    purchases = relationship("Purchase", back_populates="user")

    inventory_logs = relationship(
        "InventoryLog",
        back_populates="performed_by_user"
    )


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)

    make = Column(String(100), nullable=False)

    model = Column(String(100), nullable=False)

    category = Column(String(50), nullable=False)

    price = Column(Numeric(12, 2), nullable=False)

    quantity = Column(Integer, nullable=False)

    purchases = relationship("Purchase", back_populates="vehicle")

    inventory_logs = relationship(
        "InventoryLog",
        back_populates="vehicle"
    )


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE")
    )

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id", ondelete="CASCADE")
    )

    quantity = Column(Integer)

    total_price = Column(Numeric(12, 2))

    purchased_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    user = relationship("User", back_populates="purchases")

    vehicle = relationship("Vehicle", back_populates="purchases")


class InventoryLog(Base):
    __tablename__ = "inventory_logs"

    id = Column(Integer, primary_key=True)

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id", ondelete="CASCADE")
    )

    performed_by = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE")
    )

    action = Column(String(20))

    quantity = Column(Integer)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="inventory_logs"
    )

    performed_by_user = relationship(
        "User",
        back_populates="inventory_logs"
    )