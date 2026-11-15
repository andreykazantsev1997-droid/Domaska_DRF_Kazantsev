from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from materials.models import Courses, Lessons
from users.models import Subscription

User = get_user_model()


class LessonTestCase(APITestCase):

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом"""
        self.user = User.objects.create(email="test@test.com")
        self.user.set_password("testpassword")
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Courses.objects.create(
            title="Тестовый курс", description="Описание тестового курса", owner=self.user
        )

        self.lesson = Lessons.objects.create(
            title="Тестовый урок",
            description="Описание урока",
            course=self.course,
            owner=self.user,
        )

    def test_lesson_create(self):
        """Тест создания урока"""
        url = reverse("materials:lesson-create")
        data = {
            "title": "Новый урок",
            "description": "Описание нового урока",
            "course": self.course.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lessons.objects.count(), 2)

    def test_lesson_list(self):
        """Тест получения списка уроков (с учетом пагинации)"""
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.json())

    def test_lesson_retrieve(self):
        """Тест получения детальной информации об уроке"""
        url = reverse("materials:lesson-get", args=(self.lesson.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], self.lesson.title)

    def test_lesson_update(self):
        """Тест обновления урока"""
        url = reverse("materials:lesson-update", args=(self.lesson.id,))
        data = {"title": "Обновленный урок"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, "Обновленный урок")

    def test_lesson_delete(self):
        """Тест удаления урока"""
        url = reverse("materials:lesson-delete", args=(self.lesson.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lessons.objects.count(), 0)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        """Подготовка данных для тестирования подписок"""
        self.user = User.objects.create(email="sub_test@test.com")
        self.user.set_password("password")
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Courses.objects.create(
            title="Курс для подписки", description="Описание", owner=self.user
        )

    def test_subscription_toggle(self):
        """Тест добавления и удаления подписки на курс"""
        url = "/users/subscriptions/"
        data = {"course_id": self.course.id}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "подписка добавлена")
        self.assertTrue(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["message"], "подписка удалена")
        self.assertFalse(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )