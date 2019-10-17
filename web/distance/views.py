from .models import Cords
from django.shortcuts import render
from .forms import Info
from .helper import calc
import csv, io
from django.contrib import messages


def index(request):
    form = Info(request.GET)
    return render(request, 'distance/index.html', {'forms': form})


def detail(request):
    form = request.GET
    print(form)

    cord = Cords.objects.all()
    latitude = form.get("latitude")
    longitude = form.get("longitude")
    range_ = form.get("range")
    context = {
       'cord': cord,
       'range': range_,
    }
    for cords in cord:
        cords.dis = calc(float(cords.longitude), float(longitude), float(cords.longitude), float(latitude))
    if Info(request.GET).is_valid():
        return render(request, 'distance/answer.html', context)
