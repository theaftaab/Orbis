from fastapi import APIRouter

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


