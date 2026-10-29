from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import Courses, Lessons
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email

class Payments(models.Model):
    CASH = 'cash'
    TRANSFER = 'transfer'

    PAYMENT_METHODS = (
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Оплаченный курс')
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Оплаченный урок')
    payment = models.IntegerField(verbose_name='Сумма оплаты')
    method =models.CharField(choices=PAYMENT_METHODS, max_length=20, verbose_name='Метод оплаты')
