# Inventory & Order Management System

A production-ready full-stack application for managing products, customers, and orders with real-time inventory tracking. Built with FastAPI, React, PostgreSQL, and Docker.

## 🚀 Features

### Product Management
- ✅ Create, read, update, and delete products
- ✅ Unique SKU tracking
- ✅ Real-time inventory management
- ✅ Automatic stock updates on order placement

### Customer Management
- ✅ Customer profile management
- ✅ Email validation and uniqueness
- ✅ Contact information tracking

### Order Management
- ✅ Create orders with multiple items
- ✅ Automatic inventory deduction
- ✅ Automatic order total calculation
- ✅ Order cancellation with inventory restoration

### Dashboard
- ✅ Key metrics (products, customers, orders, revenue)
- ✅ Low stock alerts
- ✅ Recent orders overview
- ✅ Real-time data updates

## 📋 Tech Stack

### Backend
- **Python 3.11** - Programming language
- **FastAPI** - Modern async web framework
- **SQLAlchemy** - ORM for database
- **Pydantic** - Data validation
- **PostgreSQL** - Relational database

### Frontend
- **React 18** - UI library
- **React Router v6** - Navigation
- **Axios** - HTTP client
- **CSS3** - Styling

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (React)                         │
│              http://localhost:3000                           │
└─────────────────────────┬───────────────────────────────────┘
                          │
                    HTTP/REST
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                 Backend (FastAPI)                            │
│           http://localhost:8000                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
                      SQLAlchemy
                          │
┌─────────────────────────▼───────────────────────────────────┐
│            PostgreSQL Database                               │
│    localhost:5432                                            │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git

### Local Development with Docker

```bash
# Clone the repository
git clone https://github.com/adityayadav6299/AI-Chatbot-Backend.git
cd AI-Chatbot-Backend

# Create environment file
cp .env.example .env

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

## 📚 API Documentation

### Base URL
- **Local**: `http://localhost:8000`

### Endpoints

#### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | Get all products |
| GET | `/products/{id}` | Get product by ID |
| POST | `/products` | Create new product |
| PUT | `/products/{id}` | Update product |
| DELETE | `/products/{id}` | Delete product |

#### Customers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/customers` | Get all customers |
| GET | `/customers/{id}` | Get customer by ID |
| POST | `/customers` | Create new customer |
| PUT | `/customers/{id}` | Update customer |
| DELETE | `/customers/{id}` | Delete customer |

#### Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/orders` | Get all orders |
| GET | `/orders/{id}` | Get order by ID |
| POST | `/orders` | Create new order |
| DELETE | `/orders/{id}` | Cancel order |

#### Dashboard
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dashboard` | Get dashboard metrics |

## 🔐 Business Logic

### Inventory Management
- **Stock Validation**: Cannot create products with negative stock
- **Order Validation**: Orders cannot be placed if inventory is insufficient
- **Auto-Deduction**: Stock automatically reduces when orders are created
- **Restoration**: Stock is restored when orders are cancelled

### Data Integrity
- **SKU Uniqueness**: Product SKU must be unique
- **Email Uniqueness**: Customer email must be unique
- **Automatic Calculation**: Order total calculated automatically
- **Cascading Deletes**: Related data cleaned up on deletion

## 📦 Environment Variables

Create a `.env` file:

```env
# Database Configuration
DATABASE_URL=postgresql://postgres:postgres@db:5432/inventory_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=inventory_db

# Backend Configuration
BACKEND_URL=http://backend:8000
API_PORT=8000
DEBUG=False

# Frontend Configuration
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_TIMEOUT=30000
```

## 🐳 Docker Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Rebuild images
docker-compose build --no-cache
```

## 📊 Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   └── routes/
│   │       ├── products.py
│   │       ├── customers.py
│   │       ├── orders.py
│   │       └── dashboard.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Products.jsx
│   │   │   ├── Customers.jsx
│   │   │   └── Orders.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── index.css
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── Dockerfile
│   └── .dockerignore
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Deployment

### Backend (Render/Railway/Fly.io)
1. Push code to GitHub
2. Connect to hosting platform
3. Set environment variables
4. Deploy

### Frontend (Vercel/Netlify)
1. Push code to GitHub
2. Connect to Vercel/Netlify
3. Set `REACT_APP_API_URL` environment variable
4. Deploy

## 📝 License

MIT License

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 💬 Support

For issues and questions:
- Open an issue on GitHub
- Review API documentation at `/docs`

---

**Made with ❤️ by Aditya Yadav**
