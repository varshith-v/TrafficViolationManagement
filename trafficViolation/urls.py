from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('dlRegister',views.dlRegister, name = 'dlRegsiter'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('service',views.service,name='service'),
    path('user_login',views.user_login, name = 'user_login'),
    path('official_login',views.official_login,name="official_login"),
    path('complaint',views.lodge_complaint, name="complaint"),
    path('dlRegister_page',views.dlRegister_page,name="dlRegister_page"),
    path('pay',views.pay,name="pay"),
    path('vehicleReg_page',views.vehicleReg_page,name="vehicleReg_page"),
    path('complaint_page',views.complaint_page,name = "complaint_page")
] 