from fastapi import APIRouter, Depends

from SharedBackend.managers import *

from models import *
from config import get_settings, get_engine
from utils import dependencies as D

settings = get_settings()
engine = get_engine(settings.name)
api_key_manager = ApiKeyManager(engine)

router = APIRouter(dependencies=[Depends(D.master_key_dependency)])


@router.get("/health-check")
async def health_check():
    return HealthCheckResponse(
        status=f"{settings.name}[node:{0}/{0}] is running with {0}/{0} passing",
        version=settings.version,
        commit=settings.commit,
        branch=settings.branch,
        build_time=settings.build_time,
        build_number=settings.build_number,
        build_tags=settings.build_tags,
    )


@router.post("/generate-api-key", response_model=GenerateApiKeyResponse)
async def generate_api_key(payload: GenerateApiKeyRequest):
    api_key = api_key_manager.generate_key()
    key_record = await api_key_manager.register_key(api_key, *payload.scopes)
    return GenerateApiKeyResponse(
        uid=key_record.uid,
        key=api_key,
        scopes=payload.scopes,
    )


@router.delete("/revoke-api-key/{uid}", response_model=StatusResponse)
async def revoke_api_key(uid: str):
    await api_key_manager.delete(uid)
    return StatusResponse()
