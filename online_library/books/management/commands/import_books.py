import json
from django.core.management.base import BaseCommand
from books.models import Book


class Commande(BaseCommand):
    help = 'Loads books from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file.')

    def handle(self, *args, **options):
        json_file = options['json_file']

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(f'Error reading file: {e}')
            return

        for entry in data:
            if entry['model'] == 'books.book':
                book_data = entry['fields']
                try:
                    book = Book.objects.create(
                        name=book_data['name'],
                        author=book_data['author'],
                        pub_date=book_data['pub_date'],
                    )
                    self.stdout.write(f'Created book: {book.name}')
                except Exception as e:
                    self.stderr.write(f'Error adding book {book_data["name"]}: {e}')
