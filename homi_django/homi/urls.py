# homi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('items/', views.item_list, name='item_list'),
    path('rooms/<int:pk>', views.room_detail, name='room_detail'),
    path('items/<int:pk>', views.item_detail, name='item_detail'),
    path('rooms/new', views.room_create, name='room_create'), 
    path('items/new', views.item_create, name='item_create'), 
    path('rooms/<int:pk>/edit', views.room_edit, name='room_edit'),
    path('items/<int:pk>/edit', views.item_edit, name='item_edit'),
    path('rooms/<int:pk>/delete', views.room_delete, name='room_delete'),


]
