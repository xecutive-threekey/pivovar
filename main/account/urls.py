from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('', views.home, name='home'),
]