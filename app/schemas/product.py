from pydantic import BaseModel, Field
from enum import Enum

class CategoryEnum(str, Enum):
    apparel = "Apparel"
    home = "Home"
    electronics = "Electronics"

class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=255)
    category: CategoryEnum
    price: float = Field(..., gt=0)

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
