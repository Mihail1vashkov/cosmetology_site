import json
from django.core.management.base import BaseCommand
from cosmetology.models import Procedure
import pytz
from datetime import datetime

class Command(BaseCommand):
    help = 'Load procedures from procedures.json'

    def handle(self, *args, **kwargs):
        with open('procedures.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                # Преобразование наивного datetime в aware datetime
                naive_datetime = datetime.strptime(item['appointment_time'], '%Y-%m-%d %H:%M:%S')
                aware_datetime = pytz.timezone('UTC').localize(naive_datetime)

                Procedure.objects.create(
                    name=item['name'],
                    description=item['description'],
                    appointment_time=aware_datetime
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded procedures'))
