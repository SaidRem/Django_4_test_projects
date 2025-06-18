import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    help = 'Imports phones from csv file to Phone model.'
    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to csv file.')

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        self.stdout.write(f'Start import from file: {csv_path}')

        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                phone_id = row['id']
                try:
                    phone = Phone.objects.get(id=phone_id)
                    # Update entry
                    phone.name = row['name']
                    phone.image = row['image']
                    phone.price = row['price']
                    phone.release_date = row['release_date']
                    phone.lte_exists = row['lte_exists'] == 'True'
                    phone.slug = slugify(row['name'])
                    phone.save()
                    msg = f'Updated: {phone.name}'
                except Phone.DoesNotExist:
                    # Create entry
                    phone = Phone.objects.create(
                        id=phone_id,
                        name=row['name'],
                        image=row['image'],
                        price=row['price'],
                        release_date=row['release_date'],
                        lte_exists=row['lte_exists'] == 'True',
                        slug=slugify(row['name']),
                    )
                    msg = f'Created: {phone.name}'

                self.stdout.write(msg)
