from fastapi import APIRouter
from app.models.dashboard_models import DashboardStats

router = APIRouter()

@router.get("/", response_model=DashboardStats, tags=["Dashboard"], summary="Get Dashboard Summary")
def get_dashboard():
    return DashboardStats(
        breaches_detected=15,
        active_threats=1,
        system_health="Excellent"
    )
