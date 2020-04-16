# homi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('items/', views.item_list, name='item_list')
]
