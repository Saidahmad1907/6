from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Brand, Car

def all_brands_and_cars(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'all_brands_and_cars.html', {'brands': brands, 'cars': cars})

def brand_cars(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = brand.cars.all()
    return render(request, 'brand_cars.html', {'brand': brand, 'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})
