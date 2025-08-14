from fastapi import APIRouter

from config import get_engine, get_settings
from managers import *

router = APIRouter(prefix="/examples")
settings = get_settings()
engine = get_engine(settings.name)

example_manager = ExampleManager(engine)


@router.post("", response_model=ExampleSchema.__model__)
async def post_example(payload: ExampleSchema.__post_model__):
    async with example_manager.session_factory() as session:
        example_record = await example_manager.create(
            payload,
            session=session,
        )
        await session.commit()
    return example_record.model_dump(sanitize=True)
