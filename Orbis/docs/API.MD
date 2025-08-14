## API Documentation

### **Base URL**
All endpoints are prefixed with `api//v1`.

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

### **Many-to-One Foreign**

#### **Create Many-to-One Foreign**
- **URL**: `/examples/{exampleId}/many-to-one-foreign`
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
    "example_uid": "string"
  }
  ```

#### **Fetch Many-to-One Foreign**
- **URL**: `/examples/many-to-one-foreign/{uid}`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "uid": "string",
    "created_at": "datetime",
    "updated_at": "datetime",
    "message": "string",
    "example_uid": "string"
  }
  ```

---

### **One-to-One Foreign**

#### **Create One-to-One Foreign**
- **URL**: `/examples/{exampleId}/one-to-one-foreign`
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
    "example_uid": "string"
  }
  ```

---

### **Many-to-Many Foreign**

#### **Create Many-to-Many Foreign**
- **URL**: `/examples/{exampleId}/many-to-many-foreign`
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
    "examples": []
  }
  ```

---

### **One-to-Many Foreign**

#### **Create One-to-Many Foreign**
- **URL**: `/examples/{exampleId}/one-to-many-foreign`
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
    "examples": []
  }
  ```

---

This documentation provides a comprehensive overview of the code structure and API endpoints. For more details, refer to the code comments and inline documentation.
