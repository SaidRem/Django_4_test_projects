import csv
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render


def bus_stations(request):
    page_number = request.GET.get('page', 1)

    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        stations = list(reader)

    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)

    # Smart pagination: +/-2 pages around current
    total_pages = paginator.num_pages
    current = page.number
    page_range = []

    if total_pages <= 7:
        page_range = range(1, total_pages + 1)
    else:
        if current <= 4:
            page_range = list(range(1, 6)) + ['...', total_pages]
        elif current >= total_pages - 3:
            page_range = [1, '...'] + list(range(total_pages - 4, total_pages + 1))
        else:
            page_range = [1, '...'] + list(range(current - 2, current + 3)) + ['...', total_pages]

    context = {
        'bus_stations': page.object_list,
        'page': page,
        'page_range': page_range
    }
    return render(request, 'stations/index.html', context)
