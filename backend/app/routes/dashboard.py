from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models import Product, Customer, Order
from app.schemas import DashboardMetrics

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("", response_model=DashboardMetrics)
async def get_dashboard_metrics(db: Session = Depends(get_db)):
    """Get dashboard metrics"""
    
    # Total counts
    total_products = db.query(func.count(Product.id)).scalar() or 0
    total_customers = db.query(func.count(Customer.id)).scalar() or 0
    total_orders = db.query(func.count(Order.id)).scalar() or 0
    
    # Total revenue
    total_revenue = db.query(func.sum(Order.total_amount)).scalar() or 0
    
    # Low stock products (less than 10 units)
    low_stock = db.query(Product).filter(Product.quantity_in_stock < 10).all()
    
    # Recent orders (last 5)
    recent_orders = db.query(Order).order_by(Order.created_at.desc()).limit(5).all()
    
    return DashboardMetrics(
        total_products=total_products,
        total_customers=total_customers,
        total_orders=total_orders,
        total_revenue=float(total_revenue),
        low_stock_products=low_stock,
        recent_orders=recent_orders
    )
