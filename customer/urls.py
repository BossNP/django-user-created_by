from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('customer/api/', views.CustomerAPI),
    path('customer/api/<int:pk>/', views.CustomerAPI),
    path('gender/api/', views.GenderAPI),
    path('gender/api/<int:pk>/', views.GenderAPI),
]