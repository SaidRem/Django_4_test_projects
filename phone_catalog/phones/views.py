from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'phones/catalog.html'

    sort_val = request.GET.get('sort')

    if sort_val == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_val == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_val == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'phones/product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
