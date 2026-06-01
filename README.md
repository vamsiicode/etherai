# Inventory & Order Management System

This project is a small inventory and order management system. The backend is built with FastAPI and the frontend is built with React. There is also a local Docker setup so you can run everything together.

The backend handles products, customers and orders, with stock tracking and basic validation. The frontend is a simple React app that talks to the API and lets you manage the data.

## Project structure
The backend code is in the `backend` folder and the frontend code is in the `frontend` folder. There is also a `docker-compose.yml` file at the root for running the full app locally.

## Run locally
If you want to run the app on your machine, first copy `.env.example` to `.env` in the backend folder. By default the backend uses SQLite when `DB_TYPE=sqlite`.

To start the backend locally, go to the `backend` folder and run the app with uvicorn. Then go to the `frontend` folder and start the React dev server.

The backend should be available on `http://localhost:8000` and the frontend on `http://localhost:5173`. The API docs are available at `http://localhost:8000/docs`.

If you have Docker Desktop and want to use PostgreSQL, set `DB_TYPE=postgres` in `backend/.env`, then run `docker compose up --build` from the project root.

## Docker Hub publishing
There is a workflow in `.github/workflows/dockerhub-publish.yml` that can publish the backend image to Docker Hub when the right secrets are set.

The secrets are named `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`. If those are not set, the workflow will now stop and tell you which secret is missing.

When it works, the backend image is pushed as `docker.io/<your-username>/inventory-order-system-backend:latest`.

## Frontend deployment
There is also a workflow for deploying the frontend to GitHub Pages, and it builds the app for a project site at `/etherai/`.

To use that, the site needs to be enabled from the repository Pages settings and the workflow must be allowed to publish to the `gh-pages` branch.

## Backend deployment to Render
The backend has a workflow that can trigger a Render deploy when `RENDER_SERVICE_ID` and `RENDER_API_KEY` are set.

That workflow does not deploy by itself until those secrets are added and a Render service is configured to use this repository.

## Running only the backend
If you just want the backend and not Docker, make sure PostgreSQL is running locally and set `POSTGRES_HOST=localhost` in `backend/.env`. Then start the backend from the `backend` folder with uvicorn.

If you want, I can also make this README even more conversational and remove the remaining technical formatting so it feels even less robotic.