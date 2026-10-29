from django.shortcuts import render
from rest_framework import viewsets, generics

from materials.models import Courses, Lessons
from materials.serializers import CoursesSerializer, LessonsSerializer


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