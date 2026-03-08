Task Manager
A simple full-stack task manager built using:

FastAPI (Backend API)
Vue 3 + Vite (Frontend)
PostgreSQL (Database)
Redis + Celery (Background worker)
Docker Compose
The application allows users to manage tasks and view dashboard statistics.

Features
User registration and login using JWT authentication
Create, update, and delete tasks
Task description and status management
Filter tasks by status
Pagination for task listing
Dashboard showing counts for:
Todo
In Progress
Done
Admin users can view all registered users
Background worker using Celery with Redis
Create a .env file from .env.example.

SECRET_KEY=supersecretkey DATABASE_URL=postgresql://postgres:postgres@db:5432/tasks ACCESS_TOKEN_EXPIRE_MINUTES=60

Run the Project

docker compose up--build


screenshots
<img width="1919" height="805" alt="Screenshot 2026-03-08 122129" src="https://github.com/user-attachments/assets/a101e95b-2621-40ed-a3e8-c05f4ec4dbd7" />


<img width="1919" height="857" alt="Screenshot 2026-03-08 122114" src="https://github.com/user-attachments/assets/16832ac0-3fb4-40f7-8825-2d74caed5ce2" />

<img width="1919" height="842" alt="Screenshot 2026-03-08 123231" src="https://github.com/user-attachments/assets/734f0fb7-c9bd-498e-a449-306ffd69f00e" />

