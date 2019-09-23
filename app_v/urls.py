from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginPage, name='login'),
    path('VehicleReg',views.registerVehicle, name='VehicleReg'),
    path('auth',views.authOfficer, name='auth')
]