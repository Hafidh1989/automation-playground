from typing import List
from pydantic import BaseModel, EmailStr

class dimensions(BaseModel):
    width: float
    height: float
    depth: float

class Review(BaseModel):
    rating: int
    comment: str
    date:str
    reviewerName:str
    reviewerEmail:str

class Meta(BaseModel):
    createdAt: str
    updatedAt: str
    barcode: str
    qrCode: str

class Product(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    tags: List[str]
    brand: str
    sku: str
    weight: int
    dimensions: dimensions
    warrantyInformation: str
    shippingInformation: str
    availabilityStatus: str
    reviews: List[Review]
    returnPolicy: str
    minimumOrderQuantity: int
    meta: Meta
    thumbnail: str
    images: List[str]

class ProductListResponse(BaseModel):
    products: List[Product]
    total: int
    skip: int
    limit: int