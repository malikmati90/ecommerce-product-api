from sqlalchemy import Column, Integer, Numeric, String
from app.core.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)
    category = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

