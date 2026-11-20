from datetime import timedelta
from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import CustomUser

@shared_task
def check_inactive_users():
    User = get_user_model()
    time = timezone.now() - timedelta(days=30)
    inactive_users =User.objects.filter(is_active = True, last_login__lt=time)
    inactive_users.update(is_active = False)