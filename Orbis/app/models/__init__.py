from pydantic import BaseModel

from .generateApiKeyModels import *
from .healthCheckModels import *
from .handshakeModels import *
from .registerDriversModels import *
from .orderModels import *


class ListResponse[ModelType: BaseModel](BaseModel):
    items: list[ModelType]
    count: int


class StatusResponse(BaseModel):
    status: str = "ok"
