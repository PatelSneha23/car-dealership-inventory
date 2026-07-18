from fastapi import APIRouter

router = APIRouter()


@router.get("/vehicles")
def get_all_vehicles():
    return []