import json
from django.core.management.base import BaseCommand
from school.models import Teacher, Student


class Command(BaseCommand):
    help = 'Loads data for teachers and students from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(f"Error reading the file: {e}")
            return

        for entry in data:
            model = entry['model']
            fields = entry['fields']

            if model == 'school.teacher':
                teacher = Teacher.objects.create(
                    id=entry['pk'],
                    name=fields['name'],
                    subject=fields['subject']
                )
                self.stdout.write(f"Teacher '{teacher.name}' added.")

            elif model == 'school.student':
                student = Student.objects.create(
                    id=entry['pk'],
                    name=fields['name'],
                    teacher_id=fields['teacher'],
                    group=fields['group']
                )
                self.stdout.write(f"Student '{student.name}' added.")
