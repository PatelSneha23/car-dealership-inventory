from decimal import Decimal

from pydantic import BaseModel


class VehicleBase(BaseModel):
    make: str
    model: str
    category: str
    price: Decimal
    quantity: int


class VehicleCreate(VehicleBase):
    pass


class VehicleResponse(VehicleBase):
    id: int

    class Config:
        from_attributes = True