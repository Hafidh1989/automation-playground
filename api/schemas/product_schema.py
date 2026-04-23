from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str
    price: float


class ProductListResponse(BaseModel):
    products: List[Product]
    total: int
    skip: int
    limit: int