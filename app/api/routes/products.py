from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.crud import product
from app.schemas import Product, ProductCreate


router = APIRouter()


# GET /products and GET /products?category=Apparel
@router.get("", response_model=List[Product])
def read_products(
    db: Session = Depends(get_db),
    category: str = Query(None),
    skip: int = 0,
    limit: int = 100
):
    if category:
        return product.get_products_by_category(db, category)
    return product.get_products(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=Product)
def read_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = product.get_product_by_id(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.post("/", response_model=Product, status_code=200)
def create_new_product(product_create: ProductCreate, db: Session = Depends(get_db)):
    return product.create_product(db, product_create)
