from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import get_all_vehicles

router = APIRouter()


@router.get("/vehicles")
def read_vehicles(db: Session = Depends(get_db)):
    return get_all_vehicles(db)