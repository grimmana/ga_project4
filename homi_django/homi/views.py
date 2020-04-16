from django.shortcuts import render
from .models import Room, Item
# Create your views here.

# homi/views.py

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'homi/room_list.html', {'rooms': rooms})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'homi/item_list.html', {'items': items})

def room_detail(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'homi/room_detail.html', {'room': room})

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'homi/item_detail.html', {'item': item})    