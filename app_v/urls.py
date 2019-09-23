from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginPage, name='login'),
    path('reg',views.registerVehicle, name='reg'),
    path('auth',views.authOfficer, name='auth')
]