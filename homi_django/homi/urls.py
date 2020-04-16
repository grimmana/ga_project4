# homi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('items/', views.item_list, name='item_list'),
    path('rooms/<int:pk>', views.room_detail, name='room_detail'),
    path('items/<int:pk>', views.item_detail, name='item_detail')

]
