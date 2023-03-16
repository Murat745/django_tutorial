from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from faker import Faker

User = get_user_model()


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        users = []
        count = options['count']
        fake = Faker()
        for _ in range(count):
            user = User(username=fake.user_name(), email=fake.ascii_email(), password=make_password(fake.password()))
            users.append(user)

        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} users!'))
