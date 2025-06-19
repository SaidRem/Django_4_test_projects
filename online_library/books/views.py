from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def show_books_by_date(request, pub_date):
    books = Book.objects.filter(pub_date=pub_date).order_by('name')

    previous_date = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').last()
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

    context = {
        'books': books,
        'previous_date': previous_date.pub_date if previous_date else None,
        'next_date': next_date.pub_date if next_date else None,
    }
    return render(request, 'books/books_list.html', context)
