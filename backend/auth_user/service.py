from django.conf import settings
from django.core.mail import send_mail

def send(email, code):
    send_mail(
        subject='Subject here',
        message=f'Verification code: {code}',
        recipient_list=[email],
        from_email=settings.EMAIL_HOST_PASSWORD,
    )