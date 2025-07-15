from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def clear_dbs():
    from app.core.db import SessionLocal, engine
    from app.models import product
    product.Base.metadata.drop_all(bind=engine)
    product.Base.metadata.create_all(bind=engine)

     # Insert sample data
    db = SessionLocal()
    mock_products = [
        product.Product(name="T-shirt", category="Apparel", price=19.99),
        product.Product(name="Sneakers", category="Apparel", price=49.99),
        product.Product(name="Coffee Mug", category="Home", price=9.99),
    ]
    db.add_all(mock_products)
    db.commit()
    db.close()


def test_get_all_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product_by_id():
    response = client.get("/products/1")
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert "name" in product
    assert "category" in product
    assert "price" in product

def test_get_product_not_found():
    response = client.get("/products/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_get_products_by_category():
    response = client.get("/products?category=Apparel")
    assert response.status_code == 200
    products = response.json()
    assert all(p["category"] == "Apparel" for p in products)

def test_create_product():
    payload = {
        "name": "Test Product",
        "category": "Home",
        "price": 12.34
    }
    response = client.post("/products/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["category"] == payload["category"]
    assert data["price"] == payload["price"]
