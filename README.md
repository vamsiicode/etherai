Inventory and Order Management System

This repo has a small app that keeps track of products, customers and orders. The backend is built with FastAPI and the frontend is built with React. There is also a Docker Compose setup so you can run everything locally with a database.

The backend code is in the backend folder and the frontend code is in the frontend folder. The docker-compose.yml file at the project root starts everything together.

Running it locally

To run this on your machine, copy backend/.env.example to backend/.env. By default the backend uses SQLite.

Then go into the backend folder and start the backend server with uvicorn. In another terminal open the frontend folder and start the React dev server.

The frontend should open at http://localhost:5173 and the backend docs should be available at http://localhost:8000/docs.

If you want to use PostgreSQL with Docker Desktop, set DB_TYPE=postgres in backend/.env and run docker compose up --build from the project root. That will start the database, backend, and frontend together.

Docker Hub publishing

There is a GitHub Actions workflow in .github/workflows/dockerhub-publish.yml that can publish the backend Docker image to Docker Hub.

To make that work, add two repository secrets named DOCKERHUB_USERNAME and DOCKERHUB_TOKEN. After that the workflow can log in and push the image.

The image will be published as docker.io/your-username/inventory-order-system-backend:latest.

Frontend deployment

There is also a workflow for deploying the frontend to GitHub Pages. It builds the frontend and publishes it to the gh-pages branch.

That workflow needs GitHub Pages enabled in the repository settings and permission to publish to the branch.

Backend deployment to Render

A separate workflow can trigger a Render deployment if you add RENDER_SERVICE_ID and RENDER_API_KEY as repository secrets.

That workflow will not deploy anything until those secrets are set and a Render service is configured for this repo.

If you only want the backend

If you only want to run the backend without Docker, make sure PostgreSQL is running locally and set POSTGRES_HOST=localhost in backend/.env.

Then start the backend from the backend folder with uvicorn.
