import sqlalchemy as db

from SharedBackend.managers import BaseSchema, GenericManager


class ExampleSchema(BaseSchema):
    __tablename__ = "examples"

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    migration_test = db.Column(db.String, nullable=False, server_default="migration-test")


class ExampleManager(GenericManager[ExampleSchema]):
    pass


__all__ = [
    "ExampleSchema", "ExampleManager",
]
