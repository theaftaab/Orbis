## Verbose Documentation

### **Overview**
The code is divided into several modules:
- **`manager.py`**: Contains the database schema definitions, models, and managers for handling database operations.
- **`v1.py`**: Defines the FastAPI routes and handlers for the API endpoints.
- **`models.py`**: Contains Pydantic models for request and response validation.
- **`base.py`**: Provides base classes for database schemas, models, and managers.

The application uses SQLAlchemy for ORM (Object-Relational Mapping) and FastAPI for building the REST API. It supports CRUD operations for entities with various relationships.

---

### **Database Schema and Models**

#### **Association Table**
- **`association_table`**: A many-to-many relationship table that links `examples` and `many-to-many-foreign` tables.

#### **Schemas**
- **`ManyToOneForeignSchema`**: Represents a many-to-one relationship with the `examples` table.
- **`ManyToManyForeignSchema`**: Represents a many-to-many relationship with the `examples` table.
- **`OneToOneForeignSchema`**: Represents a one-to-one relationship with the `examples` table.
- **`OneToManyForeignSchema`**: Represents a one-to-many relationship with the `examples` table.
- **`ExampleSchema`**: The main entity schema that includes relationships with all other schemas.

#### **Models**
- **`ManyToOneForeignModel`**: Pydantic model for `ManyToOneForeignSchema`.
- **`ManyToManyForeignModel`**: Pydantic model for `ManyToManyForeignSchema`.
- **`OneToOneForeignModel`**: Pydantic model for `OneToOneForeignSchema`.
- **`OneToManyForeignModel`**: Pydantic model for `OneToManyForeignSchema`.
- **`ExampleModel`**: Pydantic model for `ExampleSchema`.

---

### **Managers**
- **`GenericManager`**: A generic manager class that provides CRUD operations for any schema and model.
- **`ExampleManager`**: A manager class for the `ExampleSchema` and `ExampleModel`. It includes sub-managers for handling related entities:
  - `ManyToOneForeignManager`
  - `OneToOneForeignManager`
  - `ManyToManyForeignManager`
  - `OneToManyForeignManager`

---

### **API Endpoints**
The API is defined in `v1.py` and provides the following endpoints:

#### **Examples**
- **POST `/examples`**: Create a new example.
- **GET `/examples/options`**: Fetch available options for examples.
- **GET `/examples/{uid}`**: Fetch a specific example by UID.
- **PATCH `/examples/{uid}`**: Update a specific example by UID.
- **DELETE `/examples/{uid}`**: Delete a specific example by UID.

#### **Many-to-One Foreign**
- **POST `/examples/{exampleId}/many-to-one-foreign`**: Create a many-to-one foreign entity.
- **GET `/examples/many-to-one-foreign/options`**: Fetch available options for many-to-one foreign entities.
- **GET `/examples/{exampleId}/many-to-one-foreign`**: Fetch many-to-one foreign entities for a specific example.
- **GET `/examples/many-to-one-foreign/{uid}`**: Fetch a specific many-to-one foreign entity by UID.
- **PATCH `/examples/many-to-one-foreign/{uid}`**: Update a specific many-to-one foreign entity by UID.
- **DELETE `/examples/many-to-one-foreign/{uid}`**: Delete a specific many-to-one foreign entity by UID.

#### **One-to-One Foreign**
- **POST `/examples/{exampleId}/one-to-one-foreign`**: Create a one-to-one foreign entity.
- **GET `/examples/one-to-one-foreign/options`**: Fetch available options for one-to-one foreign entities.
- **GET `/examples/{exampleId}/one-to-one-foreign`**: Fetch a one-to-one foreign entity for a specific example.
- **GET `/examples/one-to-one-foreign/{uid}`**: Fetch a specific one-to-one foreign entity by UID.
- **PATCH `/examples/one-to-one-foreign/{uid}`**: Update a specific one-to-one foreign entity by UID.
- **DELETE `/examples/one-to-one-foreign/{uid}`**: Delete a specific one-to-one foreign entity by UID.

#### **Many-to-Many Foreign**
- **POST `/examples/{exampleId}/many-to-many-foreign`**: Create a many-to-many foreign entity.
- **GET `/examples/many-to-many-foreign/options`**: Fetch available options for many-to-many foreign entities.
- **GET `/examples/{exampleId}/many-to-many-foreign`**: Fetch many-to-many foreign entities for a specific example.
- **GET `/examples/many-to-many-foreign/{uid}`**: Fetch a specific many-to-many foreign entity by UID.
- **PATCH `/examples/many-to-many-foreign/{uid}`**: Update a specific many-to-many foreign entity by UID.
- **DELETE `/examples/many-to-many-foreign/{uid}`**: Delete a specific many-to-many foreign entity by UID.

#### **One-to-Many Foreign**
- **POST `/examples/{exampleId}/one-to-many-foreign`**: Create a one-to-many foreign entity.
- **GET `/examples/one-to-many-foreign/options`**: Fetch available options for one-to-many foreign entities.
- **GET `/examples/{exampleId}/one-to-many-foreign`**: Fetch a one-to-many foreign entity for a specific example.
- **GET `/examples/one-to-many-foreign/{uid}`**: Fetch a specific one-to-many foreign entity by UID.
- **PATCH `/examples/one-to-many-foreign/{uid}`**: Update a specific one-to-many foreign entity by UID.
- **DELETE `/examples/one-to-many-foreign/{uid}`**: Delete a specific one-to-many foreign entity by UID.

---

## 2. **API Documentation**

### **Base URL**
All endpoints are prefixed with `/v1`.

---

### **Examples**

#### **Create Example**
- **URL**: `/examples`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "message": "string"
  }
  ```
- **Response**:
  ```json
  {
    "uid": "string",
    "created_at": "datetime",
    "updated_at": "datetime",
    "message": "string",
    "many_to_one_foreign": [],
    "one_to_one_foreign": null,
    "many_to_many_foreign": [],
    "one_to_many_foreign_id": null
  }
  ```

#### **Fetch Example**
- **URL**: `/examples/{uid}`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "uid": "string",
    "created_at": "datetime",
    "updated_at": "datetime",
    "message": "string",
    "many_to_one_foreign": [],
    "one_to_one_foreign": null,
    "many_to_many_foreign": [],
    "one_to_many_foreign_id": null
  }
  ```

#### **Update Example**
- **URL**: `/examples/{uid}`
- **Method**: `PATCH`
- **Request Body**:
  ```json
  {
    "message": "string"
  }
  ```
- **Response**:
  ```json
  {
    "uid": "string",
    "created_at": "datetime",
    "updated_at": "datetime",
    "message": "string",
    "many_to_one_foreign": [],
    "one_to_one_foreign": null,
    "many_to_many_foreign": [],
    "one_to_many_foreign_id": null
  }
  ```

#### **Delete Example**
- **URL**: `/examples/{uid}`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "status": "success"
  }
  ```

---

This documentation provides a comprehensive overview of the code structure and API endpoints. For more details, refer to the code comments and inline documentation.
