from fastapi import APIRouter

router = APIRouter()

@router.get("/{alert_id}")
def investigate_alert(alert_id: int):
    return {"id": alert_id, "status": "investigating"}
