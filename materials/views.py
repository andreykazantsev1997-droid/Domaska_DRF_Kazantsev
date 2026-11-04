from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from materials.models import Courses, Lessons
from materials.serializers import CoursesSerializer, LessonsSerializer
from users.permissions import IsModerator, IsOwnerOrStaff
# Create your views here.
class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

class LessonsCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer

class LessonsListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

class LessonsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

class LessonsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()

class LessonsDestroyAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'retrieve', 'list']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwnerOrStaff]

        return [permission() for permission in self.permission_classes]