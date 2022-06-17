import decimal, random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import Ticket


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        for _ in range(1000):
            summary = fake.paragraph(nb_sentences=1)
            details = fake.paragraph(nb_sentences=3)
            Ticket.objects.get_or_create(summary=summary, details=details)
      
