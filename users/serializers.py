from rest_framework import serializers

from materials.models import Lessons, Courses
from users.models import Payments, CustomUser, Subscription


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data, password=password)
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True)

    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Courses
        fields = ["id", "title", "description", "image", "lessons_count", "lessons", "is_subscribed"]

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user

        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False