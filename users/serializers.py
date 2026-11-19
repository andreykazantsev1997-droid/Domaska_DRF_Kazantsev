from rest_framework import serializers

from materials.models import Lessons, Courses
from users.models import Payments, CustomUser, Subscription
from users.services import create_product, create_price, create_session


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        payment = super().create(validated_data)
        product_id = create_product(payment.course)
        price_id = create_price(product_id, payment.payment)
        session_id, payment_link = create_session(price_id)

        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
        return payment


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