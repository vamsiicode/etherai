# Inventory & Order Management System

This repository contains a simple inventory and order management app. The backend is written in FastAPI and the frontend is a React app. There is also a Docker Compose setup so you can run the whole thing locally with a database.

The app is designed to keep track of products, customers and orders. It reduces inventory when orders are created and it has some basic validation so you can get a working demo quickly.

The backend lives in the `backend` folder. The frontend is in `frontend`. The `docker-compose.yml` file at the root brings everything up together.

## Running it locally

To run it locally, copy `backend/.env.example` to `backend/.env`. By default the backend uses SQLite when `DB_TYPE=sqlite`.

Then start the backend:

```bash
cd backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

In another terminal, start the frontend:

```bash
cd frontend
npm run dev
```

The frontend should load at `http://localhost:5173` and the backend docs are available at `http://localhost:8000/docs`.

If you have Docker Desktop and want to use PostgreSQL, set `DB_TYPE=postgres` in `backend/.env`, then run this from the root folder:

```bash
docker compose up --build
```

That will start PostgreSQL, the backend, and the frontend together.

## Docker Hub publishing
There is a GitHub Actions workflow at `.github/workflows/dockerhub-publish.yml` that can publish the backend Docker image to Docker Hub.

To get it working, add two repository secrets: `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`. Once those are set, the workflow can log in and push the image.

The image will be pushed as:

```text
docker.io/<your-username>/inventory-order-system-backend:latest
```

## Frontend deployment
There is also a workflow for deploying the frontend to GitHub Pages. It builds the frontend and publishes it to the `gh-pages` branch.

That needs GitHub Pages enabled in the repository settings, and the workflow needs permission to publish to the branch.

# Backend deployment to Render
A separate workflow can trigger a Render deployment if you add `RENDER_SERVICE_ID` and `RENDER_API_KEY` as repository secrets.

That workflow does not deploy anything until those secrets are configured and a Render service is set up to use this repo.

# If you only want the backend

If you just want to run the backend without Docker, make sure PostgreSQL is running locally and set `POSTGRES_HOST=localhost` in `backend/.env`.

Then start the backend with:

```bash
cd backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
