from pydantic import BaseModel

class Alert(BaseModel):
    id: int
    type: str
    severity: str
    status: str
