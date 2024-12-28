from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_brands_and_cars, name='all_brands_and_cars'),
    path('brand/<int:brand_id>/', views.brand_cars, name='brand_cars'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]
