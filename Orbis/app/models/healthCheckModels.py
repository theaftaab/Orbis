from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    status: str
    version: str
    commit: str
    branch: str
    build_time: str
    build_number: str
    build_tags: tuple


__all__ = [
    "HealthCheckResponse",
]
