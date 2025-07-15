""" Main API routes definition """
from fastapi import APIRouter, Depends
from app.api.routes import products


api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])