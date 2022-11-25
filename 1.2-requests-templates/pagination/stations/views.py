import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    def read_csv(file):
        with open(file, encoding='utf-8') as f:
            content = csv.DictReader(f)
            return list(content)

    all_bus_stations = read_csv(settings.BUS_STATION_CSV)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(all_bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
