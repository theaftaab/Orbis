from pydantic import BaseModel
from typing import Optional , Dict, Any ,List

class Drivers (BaseModel):
    driver_id: str
    name: str
    phone: str
    vehicle_class: str
    home_depot_id: str
    capacity_overrides: Dict[str, Any]
    range_km: int
    cash_in_hand_limit: int
    value_limit: Optional[int] = None
    skills: List[str] = []
    shift: Dict[str, Any]
    breaks: List[Dict[str, Any]] = []
    costs: Dict[str, Any]
    max_stops: int
    start_location: Dict[str, Any]
    end_location: Dict[str, Any]
    notes: Optional[str] = None

class RegisterDriversRequest(BaseModel):
    drivers: List[Drivers]


class RegisterDriversResponse(BaseModel):
    drivers_upserted: int
    session_id : str
    upserted_driver_ids: List[str]
    status: str = "ok"

__add__ = [
    "Drivers",
    "RegisterDriversRequest",  
    "RegisterDriversResponse",
]