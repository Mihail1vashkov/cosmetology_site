import json
from django.core.management.base import BaseCommand
from cosmetology.models import Doctor

class Command(BaseCommand):
    help = 'Load doctors from doctors.json'

    def handle(self, *args, **kwargs):
        with open('doctors.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                Doctor.objects.update_or_create(
                    name=item['name'],
                    defaults={
                        'specialization': item['specialization'],
                        'bio': item['bio']
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded doctors'))
