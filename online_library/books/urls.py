from django.urls import path, register_converter
from .views import books_view, show_books_by_date
from .converters import DateConverter


register_converter(DateConverter, 'ymd')

urlpatterns = [
    path('', books_view, name='books'),
    path('book/<ymd:pub_date>', show_books_by_date, name='book_by_date')
]
