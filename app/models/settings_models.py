from pydantic import BaseModel

class Settings(BaseModel):
    notifications_enabled: bool
    theme: str
    auto_patch: bool
