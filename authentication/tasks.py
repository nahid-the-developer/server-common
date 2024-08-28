from backend import celery_app
from django.core.mail import send_mail
from django.conf import settings


@celery_app.task()
def send_email_task():
    return 'test'
    # send_mail(
    #     subject,
    #     message,
    #     settings.DEFAULT_FROM_EMAIL,
    #     recipient_list,
    #     fail_silently=False,
    # )
