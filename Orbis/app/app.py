from contextlib import asynccontextmanager

import sqlalchemy as db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from SharedBackend.managers import ApiKeyManager, BaseSchema, EntityManager
from SharedBackend.middlewares import SDKMiddleware, EntityMiddleware
from config import get_settings, get_engine
from routers import admin_router, v1_router

settings = get_settings()
engine = get_engine(settings.name)


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        if settings.supports_schema:
            await conn.execute(db.text(f'CREATE SCHEMA IF NOT EXISTS "{settings.name}"'))
        await conn.run_sync(BaseSchema.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(admin_router, prefix="/admin")
app.include_router(v1_router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key_manager = ApiKeyManager(engine)
app.add_middleware(
    SDKMiddleware,  # type: ignore
    key_manager=api_key_manager,
)

entity_manager = EntityManager(engine)
app.add_middleware(
    EntityMiddleware,  # type: ignore
    entity_manager=entity_manager,
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("app:app", host="localhost", port=8080, reload=True)
