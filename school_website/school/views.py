from django.shortcuts import render
from django.db.models import Prefetch
from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.prefetch_related('teachers').order_by('group')
    context = {
        'students': students
    }

    return render(request, template, context)
