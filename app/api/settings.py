from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_settings():
    return {"settings": {"notification": True, "theme": "dark"}}
