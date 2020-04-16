# homi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('items/', views.item_list, name='item_list')
]

# WARNINGS:
# ?: (urls.W002) Your URL pattern '/items' [name='item_list'] has a route beginning with a '/'. Remove this slash as it is unnecessary. If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.