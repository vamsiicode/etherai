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

### Docker Hub publish workflow
A GitHub Actions workflow has been added to publish the backend Docker image to Docker Hub when the repository secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` are configured.

- Set `DOCKERHUB_USERNAME` to your Docker Hub username.
- Set `DOCKERHUB_TOKEN` to a Docker Hub access token.

The pushed image tag will be:

```text
${{ secrets.DOCKERHUB_USERNAME }}/inventory-order-system-backend:latest
```

### GitHub Pages frontend deployment
A GitHub Actions workflow has been added to build and deploy the frontend to GitHub Pages on pushes to `main`/`master`.

- The workflow publishes `frontend/dist` to the `gh-pages` branch.
- The frontend build uses `VITE_BASE=/etherai/` so it works as a GitHub Pages project site.
- Set `VITE_API_URL` in your deployed environment or in the built site if you point the frontend at a hosted backend.

After the first successful run, the site should be available at:

```text
https://<your-github-username>.github.io/etherai/
```

### Backend deployment to Render
A GitHub Actions workflow has been added to trigger a Render deploy for the backend on pushes to `main`/`master`.

- Configure a Render service to deploy the backend from Docker Hub or from your GitHub repo.
- Add the repository secrets:
  - `RENDER_SERVICE_ID` — your Render service ID
  - `RENDER_API_KEY` — your Render API key
- If your frontend is deployed to GitHub Pages, also add `VITE_API_URL` as a secret so the production build can target the hosted backend.

The Render deploy workflow is:

```text
.github/workflows/backend-deploy-render.yml
```

### Local backend only
If you want to run only the backend without Docker, ensure PostgreSQL is running locally and set `POSTGRES_HOST=localhost` in `backend/.env`.

Then start the backend with:
```bash
cd backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
