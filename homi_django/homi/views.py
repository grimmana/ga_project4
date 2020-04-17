# homi/views.py
from django.shortcuts import render, redirect
from .models import Room, Item
from .forms import RoomForm, ItemForm
# Create your views here.

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

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'homi/room_form.html', {'form': form})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'homi/item_form.html', {'form': form})

def room_edit(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'homi/item_form.html', {'form': form})

def item_edit(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'homi/item_form.html', {'form': form})

def room_delete(request, pk):
    Room.objects.get(id=pk).delete()
    return redirect('room_list')

def item_delete(request, pk):
    Item.objects.get(id=pk).delete()
    return redirect('item_list')