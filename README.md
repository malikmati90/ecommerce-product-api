## E-Commerce Product API

This is a RESTful API for managing products in an e-commerce platform. It supports retrieving all products, filtering by category, retrieving a product by ID, and creating new products with validation.

---

### Tech Stack

* **Backend Framework**: FastAPI (Python 3.11)
* **ORM**: SQLAlchemy
* **Database**: PostgreSQL (via Docker)
* **Migrations**: Yoyo
* **Testing**: Pytest, TestClient
* **Containerization**: Docker, Docker Compose
* **CI/CD**: GitHub Actions

---

### How to Run the Project

#### 1. Clone the repository

```bash
git clone https://github.com/malikmati90/ecommerce-product-api.git
cd ecommerce-product-api
```

#### 2. Run with Docker

```bash
docker compose up --build
```

This will:

* Start the FastAPI app on port `8000`
* Start PostgreSQL container
* Run migrations (including mock data)

#### 3. API Docs

Once running, visit:

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### Running Tests

```bash
docker exec -it ecommerce_api pytest
```

This will run all unit tests inside the container.

---

### Sample API Requests

#### Get all products

```bash
curl http://localhost:8000/products
```

#### Get products filtered by category

```bash
curl "http://localhost:8000/products?category=Apparel"
```

#### Get product by ID

```bash
curl http://localhost:8000/products/1
```

#### Create a new product

```bash
curl -X POST http://localhost:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Product", "category": "Home", "price": 19.99}'
```

---

### Notes

* All API responses are validated using Pydantic
* Category field supports predefined values (dropdown in Swagger)
* Docker handles all dependencies and services for local development
