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





























"""
  {
    "model": "articles.article",
    "pk": 1,
    "fields": {
      "title": "\u0412 \"\u0414\u0435\u0442\u0441\u043a\u043e\u043c \u043c\u0438\u0440\u0435\" \u043d\u0430 \u041b\u0443\u0431\u044f\u043d\u043a\u0435 \u043e\u0442\u043a\u0440\u043e\u044e\u0442 \u043c\u0443\u0437\u0435\u0439",
      "text": "\"\u0412 \u041c\u043e\u0441\u043a\u0432\u0435 \u043d\u0435\u0442 \u043c\u0443\u0437\u0435\u044f, \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0441 \u0442\u0435\u043c\u043e\u0439 \u0434\u0435\u0442\u0441\u0442\u0432\u0430, \u0438\u0433\u0440\u0443\u0448\u043a\u0438, \u0434\u0435\u0442\u0441\u043a\u0438\u043c\u0438 \u0438\u0433\u0440\u0430\u043c\u0438, \u0438 \u044d\u0442\u043e \u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u043e\u0431\u0440\u0430\u0437\u0435 \u0441\u0442\u043e\u043b\u0438\u0446\u044b\", - \u0441\u0447\u0438\u0442\u0430\u0435\u0442 \u0437\u0430\u0432\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u043c\u0443\u0437\u0435\u0439\u043d\u043e-\u0432\u044b\u0441\u0442\u0430\u0432\u043e\u0447\u043d\u044b\u043c \u043e\u0442\u0434\u0435\u043b\u043e\u043c \u0434\u0435\u043f\u0430\u0440\u0442\u0430\u043c\u0435\u043d\u0442\u0430 \u043a\u0443\u043b\u044c\u0442\u0443\u0440\u044b \u041c\u043e\u0441\u043a\u0432\u044b \u0410\u043d\u0442\u043e\u043d \u0413\u043e\u0440\u044f\u043d\u043e\u0432.",
      "published_at": "2018-09-30T19:26:52Z",
      "image": "th_946876594_EntghVT.jpg"
    }
  },
"""