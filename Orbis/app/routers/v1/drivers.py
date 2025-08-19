from fastapi import APIRouter
import random , string 
from models import *
from services import *


router = APIRouter(prefix="/sessions", tags=["drivers"])
drivers_service = RegisterDriversService()


@router.put("/{session_id}/drivers", response_model=RegisterDriversResponse)
async def upsert_drivers(session_id: str, payload: RegisterDriversRequest):
    upserted_ids = drivers_service.register_drivers(session_id,payload.drivers)
    return RegisterDriversResponse(
        drivers_upserted=len(upserted_ids),
        session_id = session_id,
        upserted_driver_ids=upserted_ids,
        status="ok",
    )

@router.post("/{session_id}/orders", response_model=OrderResponse)
async def dummy_drivers(session_id: str , payload: OrderRequest):
    character_set = string.ascii_uppercase + string.digits
    random_characters = [random.choice(character_set) for _ in range(12)] 
    run_id = "run_"+''.join(random_characters)
    orders_total = len(payload.orders)
    order_service = OrderService()
    order_service.register_orders(session_id,payload)
    OrderRes = order_service.dummy_response(run_id, orders_total)
    return OrderRes
       