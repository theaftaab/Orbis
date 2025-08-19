from pydantic import BaseModel , Field
from typing import List, Dict, Any, Optional

class Order(BaseModel):
    order_id: str
    priority: int
    type: str = Field(..., alias="type")
    location: Dict[str, Any]
    time_windows: List[ Dict[str, str]]
    service_time_min : int
    demand: Dict[str, int]
    value : Dict[str, int]
    payment_mode: str
    required_vehicle_classes: List[str]
    required_skills: List[str]

class OrderRequest(BaseModel):
    orders: List[Order]
    solve : Dict[str, Any] 

class OrderResponse(BaseModel):
    run_id: str
    status: str
    summary: Dict[str, Any]
    routes: List[Dict[str, Any]]  

__all__ = [
    "Order",
    "OrderRequest",
    "OrderResponse",
]