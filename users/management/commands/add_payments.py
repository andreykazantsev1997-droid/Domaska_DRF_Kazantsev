from django.core.management.base import BaseCommand
from users.models import Payments, CustomUser

class Command(BaseCommand):
    help ='Create payments'

    def handle(self, *args, **options):
        user = CustomUser.objects.first()
        buyers = [
            {'user': user, 'payment': 5000, 'method': 'cash'},
            {'user': user, 'payment': 4000, 'method': 'transfer'},
            {'user': user, 'payment': 3000, 'method': 'transfer'},
        ]

        for item in buyers:
            Payments.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Платежи успешно добавлены'))