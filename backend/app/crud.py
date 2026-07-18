from sqlalchemy.orm import Session

from app import models


def get_all_vehicles(db: Session):
    return db.query(models.Vehicle).all()