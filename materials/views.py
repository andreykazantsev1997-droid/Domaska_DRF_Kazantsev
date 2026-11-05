from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from materials.models import Courses, Lessons
from materials.serializers import CoursesSerializer, LessonsSerializer
from users.permissions import IsModerator, IsOwnerOrStaff
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ['update', 'partial_update', 'retrieve', 'list']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwnerOrStaff]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        return super().get_permissions()

class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ['update', 'partial_update', 'retrieve', 'list']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwnerOrStaff]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        return super().get_permissions()