from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_alerts():
    return {"alerts": [{"id": 1, "type": "malware"}, {"id": 2, "type": "phishing"}]}
