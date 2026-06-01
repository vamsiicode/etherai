from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
 
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1)
    sku: str = Field(..., min_length=1)
    stock: int = Field(..., ge=0)
    description: str | None = None
    price: int = Field(..., ge=0)

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: str | None = None

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    product_id: int
    customer_id: int
    quantity: int = Field(..., gt=0)

class ProductSummary(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CustomerSummary(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    quantity: int
    created_at: datetime
    product: ProductSummary
    customer: CustomerSummary

    class Config:
        orm_mode = True
