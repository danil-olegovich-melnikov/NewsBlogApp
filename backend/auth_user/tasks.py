from config.celery import app

from .service import send

@app.task
def send_register_code(username, code):
    print(1)
    send(username, code)