from rest_framework import serializers

from materials.models import Courses, Lessons


class CoursesSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    class Meta:
        model = Courses
        fields = '__all__'

    def get_lessons_count(self, obj):
        lessons_count = obj.lessons_set.count()
        return lessons_count

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'