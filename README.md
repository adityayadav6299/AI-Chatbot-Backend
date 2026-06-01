# Inventory & Order Management System

A production-ready full-stack application for managing products, customers, and orders with inventory tracking.

## Features

- **Product Management**: Create, read, update, and delete products with SKU tracking and inventory management
- **Customer Management**: Manage customer information with email validation
- **Order Management**: Create orders with automatic inventory deduction and order total calculation
- **Dashboard**: View key metrics including total products, customers, orders, and low-stock alerts
- **Real-time Inventory Tracking**: Automatic stock updates when orders are placed
- **Responsive Design**: Mobile-friendly React frontend
- **API Error Handling**: Comprehensive validation and error responses

## Technology Stack

### Backend
- **Python 3.11**
- **FastAPI** - Modern async web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **PostgreSQL** - Relational database

### Frontend
- **React 18** - UI library
- **Axios** - HTTP client
- **React Router** - Navigation
- **Tailwind CSS** - Styling

### Deployment & DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Render/Railway/Fly.io** - Backend hosting
- **Vercel/Netlify** - Frontend hosting

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Local Development

```bash
# Clone repository
git clone https://github.com/adityayadav6299/Inventory-Order-Management-System.git
cd Inventory-Order-Management-System

# Create environment file
cp .env.example .env

# Start all services
docker-compose up -d

# Access
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## API Endpoints

### Products
- `POST /products` - Create product
- `GET /products` - Get all products
- `GET /products/{id}` - Get product by ID
- `PUT /products/{id}` - Update product
- `DELETE /products/{id}` - Delete product

### Customers
- `POST /customers` - Create customer
- `GET /customers` - Get all customers
- `GET /customers/{id}` - Get customer by ID
- `DELETE /customers/{id}` - Delete customer

### Orders
- `POST /orders` - Create order
- `GET /orders` - Get all orders
- `GET /orders/{id}` - Get order by ID
- `DELETE /orders/{id}` - Cancel order

### Dashboard
- `GET /dashboard` - Get metrics

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   └── routes/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.jsx
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── .env.example
```

## Deployment

See deployment guides in the repository for:
- Backend deployment on Render/Railway/Fly.io
- Frontend deployment on Vercel/Netlify

## License

MIT License
