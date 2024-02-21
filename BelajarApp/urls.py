from django.urls import path, include
from . import views

# app_name = 'pertama'

urlpatterns = [
    path('', views.index, name='index'),
    
]