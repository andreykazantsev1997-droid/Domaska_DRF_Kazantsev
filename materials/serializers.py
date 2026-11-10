from rest_framework import serializers
from materials.validators import RecordValidator
from materials.models import Courses, Lessons

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True)
    description = serializers.CharField(validators=[RecordValidator(field='description')])

    class Meta:
        model = Courses
        fields = ["id", "title", "description", "image", "lessons_count", "lessons"]

    def get_lessons_count(self, obj):
        lessons_count = obj.lessons.count()
        return lessons_count