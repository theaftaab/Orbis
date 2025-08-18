from pydantic import BaseModel
from typing import Optional, Dict, Any


class HandshakeRequest(BaseModel):
    client_run_ref: str
    planning_date: str
    units: Dict[str, str]
    depot: Dict[str, Any]
    vehicle_classes: list[Dict[str, Any]]
    global_policies: Dict[str, Any]
    distance_matrix: Dict[str, Any]
    objective: Dict[str, Any]
    algorithm: Dict[str, Any]
    webhook: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, Any]] = None


class HandshakeResponse(BaseModel):
    session_id: str
    status: str
    message: str
    timestamp: str

__all__ = [
    "HandshakeRequest",
    "HandshakeResponse",
]