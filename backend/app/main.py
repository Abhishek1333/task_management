from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth_router, task_router, dashboard_router, admin_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(task_router.router)
app.include_router(dashboard_router.router)


@app.get("/")
def home():
    return {"message": "Task Manager API running"}