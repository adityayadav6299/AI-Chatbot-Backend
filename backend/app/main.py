from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import products, customers, orders, dashboard

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory & Order Management System API",
    description="A comprehensive API for managing products, customers, and orders",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(products.router)
app.include_router(customers.router)
app.include_router(orders.router)
app.include_router(dashboard.router)

@app.get("/", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Inventory & Order Management System API is running"
    }

@app.get("/api/health", tags=["health"])
async def api_health():
    """API health check"""
    return {"status": "ok", "service": "inventory-api"}
