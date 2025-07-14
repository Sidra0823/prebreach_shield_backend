from pydantic import BaseModel

class InvestigationDetail(BaseModel):
    alert_id: int
    investigator: str
    findings: str
    status: str
