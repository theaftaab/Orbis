from pydantic import BaseModel


class GenerateApiKeyRequest(BaseModel):
    scopes: list


class GenerateApiKeyResponse(BaseModel):
    uid: str
    key: str
    scopes: list


__all__ = [
    "GenerateApiKeyRequest", "GenerateApiKeyResponse",
]
