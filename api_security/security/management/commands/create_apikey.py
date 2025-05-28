from django.core.management.base import BaseCommand
from security.models import ApiKey
from security.utils import generate_api_key


class Command(BaseCommand):
    help = "Create a new global API key"

    def handle(self, *args, **kwargs):
        new_key = generate_api_key()
        ApiKey.objects.create(key=new_key, is_active=True)
        self.stdout.write(f"New API key created: {new_key}")