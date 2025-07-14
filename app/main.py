from fastapi import FastAPI
from app.api import dashboard, alerts, investigation, settings

app = FastAPI()

app.include_router(dashboard.router, prefix="/dashboard")
app.include_router(alerts.router, prefix="/alerts")
app.include_router(investigation.router, prefix="/investigation")
app.include_router(settings.router, prefix="/settings")
