from typing import List
from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate


def get_products(db: Session, skip: int, limit: int) -> List[Product]:
    return db.query(Product).offset(skip).limit(limit).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products_by_category(db: Session, category: str | None = None):
    return db.query(Product).filter(Product.category == category).all()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product