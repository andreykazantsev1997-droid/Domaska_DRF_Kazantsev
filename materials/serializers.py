from rest_framework import serializers
from materials.validators import RecordValidator
from materials.models import Courses, Lessons
from users.models import Subscription


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True)
    description = serializers.CharField(validators=[RecordValidator(field='description')])
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Courses
        fields = ["id", "title", "description", "image", "lessons_count", "lessons", "is_subscribed"]

    def get_lessons_count(self, obj):
        lessons_count = obj.lessons.count()
        return lessons_count

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False
