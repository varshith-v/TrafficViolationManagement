from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginPage, name='login'),
    path('reg',views.registerVehicle, name='reg'),
    path('auth',views.authOfficer, name='auth'),
    path('searchV',views.searchVehicle, name='searchV'),
    path('searchDL',views.searchDL, name='searchDL'),
    path('search',views.searchPage, name='searchPage'),
    path('vehicleReg',views.vehicleRegPage, name='searchDL'),
    path('dlReg',views.dlRegPage, name='searchDL'),
    path('searchComplaints',views.searchComplaints, name='searchComp'),
    path('searchCompPage',views.searchCompPage, name='searchCompPage'),
]