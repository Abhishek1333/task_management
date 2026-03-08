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

screenshots
<img width="1919" height="805" alt="Screenshot 2026-03-08 122129" src="https://github.com/user-attachments/assets/a9ded627-743e-4a1d-99da-b18e1b19d2b8" />

<img width="1919" height="857" alt="Screenshot 2026-03-08 122114" src="https://github.com/user-attachments/assets/aa5b0459-7536-4dbe-a6fd-3982f9b837f0" />

<img width="1919" height="842" alt="Screenshot 2026-03-08 123231" src="https://github.com/user-attachments/assets/14f715ba-989a-47fa-9830-58d461e3f3f3" />

