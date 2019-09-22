from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),path('dlRegister',views.dlRegister, name = 'dlRegsiter'),
    path('aboutus',views.aboutus, name='aboutus'),path('service',views.service,name='service')
] 