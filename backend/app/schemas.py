from pydantic import BaseModel, Field, EmailStr, validator
from typing import List, Optional
from datetime import datetime

# Product Schemas
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    sku: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)
    quantity_in_stock: int = Field(default=0, ge=0)
    
    @validator('name', 'sku')
    def strip_whitespace(cls, v):
        return v.strip() if isinstance(v, str) else v

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    sku: Optional[str] = Field(None, min_length=1, max_length=50)
    price: Optional[float] = Field(None, gt=0)
    quantity_in_stock: Optional[int] = Field(None, ge=0)

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    price: float
    quantity_in_stock: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Customer Schemas
class CustomerCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=20)

class CustomerUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    phone: Optional[str] = Field(None, min_length=10, max_length=20)

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Order Item Schemas
class OrderItemCreate(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float
    
    class Config:
        from_attributes = True

# Order Schemas
class OrderCreate(BaseModel):
    customer_id: int = Field(..., gt=0)
    items: List[OrderItemCreate] = Field(..., min_items=1)

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: float
    order_date: datetime
    created_at: datetime
    updated_at: datetime
    order_items: List[OrderItemResponse]
    
    class Config:
        from_attributes = True

class OrderDetailResponse(OrderResponse):
    customer: CustomerResponse

# Dashboard Schemas
class DashboardMetrics(BaseModel):
    total_products: int
    total_customers: int
    total_orders: int
    total_revenue: float
    low_stock_products: List[ProductResponse]
    recent_orders: List[OrderResponse]
