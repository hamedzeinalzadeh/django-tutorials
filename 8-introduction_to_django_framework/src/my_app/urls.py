from django.urls import path
from src.my_app import views

urlpatterns = [
    path('', views.index, name = 'index') #/my_apps --> project urls.py
]