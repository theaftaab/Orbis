from fastapi import Request, HTTPException

from config import get_settings

settings = get_settings()


def master_key_dependency(request: "Request"):
    api_key = request.headers.get("X-API-Key", "")
    if api_key != settings.master_api_key:
        raise HTTPException(status_code=403, detail="Forbidden")
