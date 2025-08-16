from fastapi import APIRouter, HTTPException

from models import *
from services import HandshakeService
from datetime import datetime

router = APIRouter(prefix="/handshake" , tags=["handshake"])
handshake_service = HandshakeService()


@router.post("", response_model=HandshakeResponse)
async def handshake(payload: HandshakeRequest ):
    """Create a new session through handshake"""
    session_id = handshake_service.create_session(payload)
    
    return HandshakeResponse(
        session_id=session_id,
        status="success",
        message="Session created successfully",
        timestamp=datetime.now().isoformat()
    )

