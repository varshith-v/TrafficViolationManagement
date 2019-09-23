from django.urls import path
from . import views

urlpatterns = [
    path('',views.searchPage, name='search'),
    #path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('reg',views.registerVehicle, name='reg'),
    path('auth',views.authOfficer, name='auth'),
    path('searchV',views.searchVehicle, name='search'),
    path('searchDL',views.searchDL, name='search1')
]