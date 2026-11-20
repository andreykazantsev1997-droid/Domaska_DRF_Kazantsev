from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from users.models import Subscription

@shared_task
def mailing_list(course_id):
    subscriptions = Subscription.objects.filter(course_id=course_id)
    emails = subscriptions.values_list("user__email", flat=True).exclude(user__email__isnull=True).exclude(user__email="")
    if not emails.exists():
        return emails
    emails = list(emails)
    send_mail("Рассылка", "Обновление курса", from_email=settings.EMAIL_HOST_USER, recipient_list=emails)

