from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


User = get_user_model()


class Command(BaseCommand):
    help = 'Delete users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('ids', nargs='+', type=int)

    def handle(self, *args, **options):
        ids = options['ids']

        if User.objects.filter(id__in=ids, is_superuser=True).exists():
            raise CommandError("Can't delete superusers")
        else:
            User.objects.filter(id__in=ids, is_superuser=False).delete()

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted user(s) with id(s) {", ".join(map(str, ids))}'))
