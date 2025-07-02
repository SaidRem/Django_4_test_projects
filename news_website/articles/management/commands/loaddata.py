import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings

from articles.models import Article


class Command(BaseCommand):
    help = 'Loads articles from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str, help='Path to JSON file')

    def handle(self, *args, **options):
        json_path = Path(options['json_path'])

        if not json_path.exists():
            self.stderr.write(self.style.ERROR(f'File {json_path} not found'))
            return

        with open(json_path, encoding='utf-8') as file:
            data = json.load(file)

            for entry in data:
                fields = entry['fields']
                image_filename = fields.get('image')

                article = Article(
                    id=entry['pk'],
                    title=fields['title'],
                    text=fields['text'],
                    published_at=fields['published_at']
                )

                if image_filename:
                    image_path = Path(settings.MEDIA_ROOT) / image_filename
                    if image_path.exists():
                        with open(image_path, 'rb') as img_file:
                            article.image.save(image_filename, File(img_file), save=False)
                    else:
                        self.stdout.write(self.style.WARNING(f'Image {image_path} not found'))
                article.save()

                self.stdout.write(self.style.SUCCESS(f'Imported: {article.title}'))
