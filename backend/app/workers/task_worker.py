from app.celery_app import celery

@celery.task
def send_task_notification(task_id: int):
    print(f"Task {task_id} created notification")
