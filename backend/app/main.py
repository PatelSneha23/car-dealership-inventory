from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routers import cars

app = FastAPI(
    title="Car Dealership Inventory API",
    version="1.0.0"
)

app.include_router(cars.router)


@app.get("/")
def root():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database();"))
        database_name = result.scalar()

    return {
        "message": "Database connected successfully!",
        "database": "car_dealership"
    }