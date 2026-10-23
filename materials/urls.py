from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views import (
    CoursesViewSet, LessonsCreateAPIView, LessonsListAPIView,
    LessonsRetrieveAPIView, LessonsUpdateAPIView, LessonsDestroyAPIView
)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonsCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/', LessonsListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='lesson-get'),
    path('lessons/update/<int:pk>/', LessonsUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/delete/<int:pk>/', LessonsDestroyAPIView.as_view(), name='lesson-delete'),
] + router.urls