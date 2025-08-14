## Developer Documentation

This documentation is intended for developers working on or extending the codebase. It provides a detailed explanation of the code structure, design patterns, and key components to help developers understand and modify the system effectively.

---

## **1. Code Structure**

The code is organized into several modules, each serving a specific purpose:

### **`manager.py`**
- **Purpose**: Defines database schemas, models, and managers for handling database operations.
- **Key Components**:
  - **Schemas**: SQLAlchemy ORM models representing database tables.
  - **Models**: Pydantic models for data validation and serialization.
  - **Managers**: Classes that encapsulate CRUD operations for each schema.

### **`v1.py`**
- **Purpose**: Defines FastAPI routes and handlers for the REST API.
- **Key Components**:
  - **Routes**: Endpoints for CRUD operations on entities and their relationships.
  - **Handlers**: Functions that process requests and interact with managers.

### **`models.py`**
- **Purpose**: Contains Pydantic models for request and response validation.
- **Key Components**:
  - **Request Models**: Define the structure of incoming request payloads.
  - **Response Models**: Define the structure of outgoing response payloads.

### **`base.py`**
- **Purpose**: Provides base classes for database schemas, models, and managers.
- **Key Components**:
  - **BaseSchema**: Base class for SQLAlchemy ORM models.
  - **BaseModel**: Base class for Pydantic models.
  - **BaseManager**: Base class for managers with common database operations.

---

## **2. Key Components**

### **Database Schemas**
- **Purpose**: Represent database tables and relationships using SQLAlchemy ORM.
- **Key Features**:
  - **Relationships**: Define one-to-one, one-to-many, many-to-one, and many-to-many relationships.
  - **Cascading**: Configure cascading behavior for related entities (e.g., delete orphaned records).
  - **Timestamps**: Automatically track creation and modification times.

#### Example Schema:
```python
class ExampleSchema(BaseSchema):
    __tablename__ = 'examples'

    message = db.Column(db.String, nullable=False)
    many_to_one_foreign = relationship('ManyToOneForeignSchema', backref='example')
    many_to_many_foreign = relationship('ManyToManyForeignSchema', secondary=association_table)
    one_to_one_foreign = relationship('OneToOneForeignSchema', backref='example', uselist=False)
    one_to_many_foreign_id = db.Column(db.String, db.ForeignKey('one-to-many-foreign.uid'))
```

---

### **Pydantic Models**
- **Purpose**: Validate and serialize data for requests and responses.
- **Key Features**:
  - **Type Validation**: Ensure data types match expected formats.
  - **Default Values**: Provide default values for optional fields.
  - **Nested Models**: Support nested models for relationships.

#### Example Model:
```python
class ExampleModel(BaseModel):
    message: Optional[str] = None
    many_to_one_foreign: list[ManyToOneForeignModel] = Field(default_factory=list)
    one_to_one_foreign: Optional[OneToOneForeignModel] = None
    many_to_many_foreign: list[ManyToManyForeignModel] = Field(default_factory=list)
    one_to_many_foreign_id: Optional[str] = None
```

---

### **Managers**
- **Purpose**: Encapsulate database operations for each schema.
- **Key Features**:
  - **CRUD Operations**: Create, read, update, and delete records.
  - **Relationship Handling**: Manage related entities and their associations.
  - **Session Management**: Handle database sessions and transactions.

#### Example Manager:
```python
class ExampleManager(GenericManager[ExampleSchema, ExampleModel]):
    class ManyToOneForeignManager(GenericManager[ManyToOneForeignSchema, ManyToOneForeignModel]):
        pass

    def __init__(self, engine):
        super().__init__(engine)
        self.many_to_one_foreign_manager = self.ManyToOneForeignManager(engine)
```

---

### **GenericManager**
- **Purpose**: Provide reusable CRUD operations for any schema and model.
- **Key Methods**:
  - **`create`**: Insert a new record into the database.
  - **`fetch`**: Retrieve a record by its UID.
  - **`update`**: Modify an existing record.
  - **`delete`**: Remove a record from the database.
  - **`fetch_all`**: Retrieve multiple records with filtering and sorting.

#### Example Usage:
```python
async def create_example(request: Request, payload: PostExampleRequest):
    example = await example_manager.create(
        ExampleModel(**payload.model_dump()), upstreamId=request.state.upstreamId
    )
    return example
```

---

## **3. API Design**

### **Endpoints**
- **Purpose**: Expose CRUD operations for entities and their relationships.
- **Key Features**:
  - **RESTful Design**: Follow REST conventions for resource management.
  - **Validation**: Use Pydantic models to validate request payloads.
  - **Error Handling**: Return appropriate HTTP status codes and error messages.

#### Example Endpoint:
```python
@router.post("/examples", response_model=ExampleModel)
async def create_example(request: Request, payload: PostExampleRequest):
    example = await example_manager.create(
        ExampleModel(**payload.model_dump()), upstreamId=request.state.upstreamId
    )
    return example
```

---

## **4. Database Relationships**

### **One-to-One**
- **Description**: A single record in one table is associated with a single record in another table.
- **Example**: `ExampleSchema` has one `OneToOneForeignSchema`.

### **One-to-Many**
- **Description**: A single record in one table is associated with multiple records in another table.
- **Example**: `OneToManyForeignSchema` has many `ExampleSchema`.

### **Many-to-One**
- **Description**: Multiple records in one table are associated with a single record in another table.
- **Example**: `ManyToOneForeignSchema` belongs to one `ExampleSchema`.

### **Many-to-Many**
- **Description**: Multiple records in one table are associated with multiple records in another table.
- **Example**: `ExampleSchema` and `ManyToManyForeignSchema` are linked via an association table.

---

## **5. Session and Transaction Management**

### **SessionFactory**
- **Purpose**: Create and manage database sessions.
- **Key Features**:
  - **Async Support**: Use asynchronous sessions for non-blocking database operations.
  - **Expire on Commit**: Prevent stale data by expiring objects after commit.

#### Example:
```python
self.session_factory = sessionmaker(
    bind=self.engine, class_=AsyncSession, expire_on_commit=False
)
```

### **Transaction Handling**
- **Purpose**: Ensure atomicity and consistency of database operations.
- **Key Features**:
  - **Context Managers**: Use `async with` to manage session lifecycle.
  - **Error Handling**: Rollback transactions on errors.

#### Example:
```python
async with self.session_factory() as session:
    data = self.model2schema(data)
    session.add(data)
    await session.commit()
```

---

## **6. Error Handling**

### **HTTP Exceptions**
- **Purpose**: Handle errors and return appropriate HTTP status codes.
- **Key Features**:
  - **404 Not Found**: Returned when a record does not exist.
  - **400 Bad Request**: Returned for invalid request payloads.
  - **500 Internal Server Error**: Returned for unexpected errors.

#### Example:
```python
async def fetch(self, uid: str, *, joins: list[QueryableAttribute] = None) -> ModelType:
    record = await session.execute(db.select(self.Schema).filter_by(uid=uid))
    if record is None:
        raise HTTPException(status_code=404, detail=f"{self.Model.__name__} not found")
```

---

## **7. Extending the Codebase**

### **Adding New Entities**
1. **Define Schema**: Create a new class in `manager.py` inheriting from `BaseSchema`.
2. **Define Model**: Create a new Pydantic model in `manager.py` inheriting from `BaseModel`.
3. **Define Manager**: Create a new manager class inheriting from `GenericManager`.
4. **Define Routes**: Add new endpoints in `v1.py` to expose CRUD operations.

### **Adding New Relationships**
1. **Update Schema**: Add relationship fields to the relevant schemas.
2. **Update Model**: Add corresponding fields to the Pydantic models.
3. **Update Manager**: Extend the manager to handle the new relationships.

---

## **8. Best Practices**

### **Code Organization**
- Keep schemas, models, and managers in `manager.py`.
- Keep API routes and handlers in `v1.py`.
- Use Pydantic models for request and response validation.

### **Error Handling**
- Use `HTTPException` to return meaningful error messages.
- Log errors for debugging and monitoring.

### **Testing**
- Write unit tests for managers and handlers.
- Use mocking to isolate database operations.

---

This developer documentation provides a comprehensive guide to understanding and extending the codebase. For further details, refer to the inline comments and type hints in the code.
