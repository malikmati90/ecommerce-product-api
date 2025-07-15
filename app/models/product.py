from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

class ProductBase(BaseModel):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category: str
    price: float

