from fastapi import APIRouter

from config import get_settings, get_engine

from models import *

from .example import router as example_router

settings = get_settings()
engine = get_engine(settings.name)

router = APIRouter()
router.include_router(example_router)


@router.get("/health-check", response_model=HealthCheckResponse)
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
