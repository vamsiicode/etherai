# Inventory & Order Management System

A simple inventory and order management app built with FastAPI, React, PostgreSQL, and Docker Compose.

## Features
- Products with unique SKU and stock count
- Customers with unique email
- Orders with stock reduction and validation
- Basic React UI to manage products, customers, and orders
- Dockerized backend, frontend, and PostgreSQL

## Project structure
- `backend/` - Python FastAPI API
- `frontend/` - React frontend
- `docker-compose.yml` - local dev stack

## Run locally
1. Copy `.env.example` to `.env`
2. By default, the backend uses local SQLite when `DB_TYPE=sqlite`.
3. Start the backend:
   ```bash
   cd backend
   .venv\Scripts\Activate.ps1
   python -m uvicorn --app-dir . app:app --reload --host 0.0.0.0 --port 8000
   ```
4. Start the frontend:
   ```bash
   cd frontend
   npm run dev
   ```
5. Open frontend at `http://localhost:5173`
6. Open API docs at `http://localhost:8000/docs`

### Docker Compose
If Docker Desktop is installed, use PostgreSQL by setting `DB_TYPE=postgres` in `backend/.env` or by using the compose override. Then run:
```bash
cd C:\Users\CHAGANTI\CODING\projects\inventory-order-system
docker compose up --build
```

The backend will be available at `http://localhost:8000` and the frontend at `http://localhost:5173`.

### Local backend only
If you want to run only the backend without Docker, ensure PostgreSQL is running locally and set `POSTGRES_HOST=localhost` in `backend/.env`.

Then start the backend with:
```bash
cd backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
