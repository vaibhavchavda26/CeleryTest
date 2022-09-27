from .models import Test
from celery import shared_task
from main import settings
from django.core.mail import send_mail

@shared_task(bind=True)
def send_mail_on_get(self):
    mail_subject = "Hi! Celery Testing for GET API"
    message = "Get Details successfully"
    to_email = "vaibhav.chavda@digiqt.com"
    send_mail(
        subject = mail_subject,
        message= message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
    )
    print("Mail From Celery usinf GET API")
    return "Done"

@shared_task(bind=True)
def send_mail_on_post(self):
    users = Test.objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing for POST API"
        message = "Details Post successfully"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message= message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    print("Mail From Celery using POST API")
    return "Done"

@shared_task(bind=True)
def send_mail_on_put(self):
    mail_subject = "Hi! Celery Testing for PUT API"
    message = "POST Details successfully"
    to_email = "vaibhav.chavda@digiqt.com"
    send_mail(
        subject = mail_subject,
        message= message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
    )
    print("Mail From Celery usinf PUT API")
    return "Done"