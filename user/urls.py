from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('user/api/', views.UserAPI),
    path('user/api/<int:pk>/', views.UserAPI),

    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token)
]