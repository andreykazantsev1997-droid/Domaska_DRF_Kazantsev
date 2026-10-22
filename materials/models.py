from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=150, verbose_name='Курс')
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.title}"

class Lessons(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=150, verbose_name='Урок')
    image = models.ImageField(upload_to='lessons/', blank=True, null=True, verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')
    video = models.URLField()

    def __str__(self):
        return f"{self.title}"