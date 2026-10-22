from django.contrib import admin
from materials.models import Courses, Lessons


# Register your models here.

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title',)

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video',)