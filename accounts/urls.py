from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.SignupView, name = 'SignupView'),
    path('registration/', views.Registration, name = 'Registration'),
    path('signout/', views.SignoutView, name = 'SignoutView'),
    

]