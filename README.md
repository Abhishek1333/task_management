# Task Manager

A simple full-stack task manager built using:

- FastAPI (Backend API)
- Vue 3 + Vite (Frontend)
- PostgreSQL (Database)
- Redis + Celery (Background worker)
- Docker Compose

The application allows users to manage tasks and view dashboard statistics.

---

## Features

- User registration and login using JWT authentication
- Create, update, and delete tasks
- Task description and status management
- Filter tasks by status
- Pagination for task listing
- Dashboard showing counts for:
  - Todo
  - In Progress
  - Done
- Admin users can view all registered users
- Background worker using Celery with Redis

---


Create a `.env` file from `.env.example`.

SECRET_KEY=supersecretkey
DATABASE_URL=postgresql://postgres:postgres@db:5432/tasks
ACCESS_TOKEN_EXPIRE_MINUTES=60

## Run the Project
docker compose up--build

