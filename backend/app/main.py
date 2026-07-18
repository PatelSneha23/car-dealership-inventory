from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI(
    title="Car Dealership Inventory API",
    version="1.0.0"
)


@app.get("/")
def root():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database();"))
        database_name = result.scalar()

    return {
        "message": "Database connected successfully!",
        "database": database_name
    }