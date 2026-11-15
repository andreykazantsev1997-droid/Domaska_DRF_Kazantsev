from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import PaymentsListAPIView, CustomUserViewSet, CustomUserCreateAPIView, SubscriptionAPIView, \
    PaymentsCreateAPIView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
app_name = 'users'

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments-create'),
    path('register/', CustomUserCreateAPIView.as_view(), name='register'),
    path('subscriptions/', SubscriptionAPIView.as_view(), name='subscription'),
] + router.urls