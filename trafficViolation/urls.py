from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),path('dlRegister',views.dlRegister, name = 'dlRegsiter'),
    path('aboutus',views.aboutus, name='aboutus'),path('service',views.service,name='service'),
    path('user_login',views.user_login, name = 'user_login'),path('official_login',views.official_login,name="official_login"),
    path('complaint',views.lodge_complaint, name="complaint")
] 