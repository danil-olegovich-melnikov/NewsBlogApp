from config.celery import app

from .service import send

@app.task
def send_register_code(username, code):
    print("HERE 2.0")
    send(username, code)