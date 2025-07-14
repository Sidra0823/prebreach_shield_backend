from pydantic import BaseModel, Field

class DashboardStats(BaseModel):
    breaches_detected: int = Field(..., description="Total number of detected breaches")
    active_threats: int = Field(..., description="Number of unresolved threats")
    system_health: str = Field(..., description="Overall system health status")
