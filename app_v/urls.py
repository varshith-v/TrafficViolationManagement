from django.urls import path
from . import views

urlpatterns = [
    path('',views.vehicleRegPage, name='home'),
    path('reg',views.registerVehicle, name='reg')
]