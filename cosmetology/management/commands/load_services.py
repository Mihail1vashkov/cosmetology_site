import json
from django.core.management.base import BaseCommand
from cosmetology.models import Service

class Command(BaseCommand):
    help = 'Load services from services.json'

    def handle(self, *args, **kwargs):
        with open('services.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                Service.objects.update_or_create(
                    name=item['name'],
                    defaults={
                        'description': item['description'],
                        'price': item['price']
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded services'))
