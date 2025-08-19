import json , random, string
from pathlib import Path
from typing import Dict, Any, List

from models.orderModels import Order, OrderRequest, OrderResponse

class OrderService:
    def __init__(self, orders_file_path: str = "orders.json"):
        self.orders_file_path = Path(orders_file_path)
        self.orders_file_path.parent.mkdir(exist_ok=True)

    def _load_orders(self) -> Dict[str, Any]:
        if not self.orders_file_path.exists():
            return {"orders": []}  
        
        try:
            with open(self.orders_file_path, 'r') as f:
                data = json.load(f)
                if not isinstance(data, list) or "orders" not in data:
                    return {"orders": []}  
                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return {"orders": []}  

    def _save_orders(self, orders: Dict[str, Any]) -> None:
        with open(self.orders_file_path, 'w') as f:
            json.dump(orders, f, indent=4)
    
    def dummy_response(self , run_id , orders_total) -> OrderResponse:

        return OrderResponse(
            run_id= run_id ,
            status="SOLVED",
            summary={"orders_total": orders_total, "routes": 3, "distance_km": 142.3},
            routes=[
                {
                    "driver_id": "drv_2w_01",
                    "route_stats": {"stops": 5, "distance_km": 42.1},
                    "waypoints": [
                        {"type": "START", "eta": "2025-08-12T08:00:00+05:30"},
                        {"type": "DELIVERY", "order_id": "ORD-1001", "eta": "2025-08-12T10:50:00+05:30"},
                        {"type": "END", "eta": "2025-08-12T15:40:00+05:30"}
                    ]
                }
            ]
        )
    def register_orders(self,session_id:str , request: OrderRequest) -> List[str]:
        orders = self._load_orders()
        orders_map = {}
        for order_item in orders:
            if isinstance(order_item, dict) and 'order_id' in order_item:
                orders_map[order_item['order_id']] = order_item

        upserted_ids: List[str] = []
        for order in request.orders:
            order_dict = order.model_dump()
            order_id = order_dict["order_id"]
            orders_map[order_id] = order_dict
            upserted_ids.append(order_id)

        self._save_orders({"session_id": session_id,"orders": list(orders_map.values()), })
        return upserted_ids