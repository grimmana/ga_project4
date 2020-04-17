# homi/forms.py
from django import forms
from .models import Room, Item

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name',)

class ItemForm(forms.ModelForm):

    class Meta:
         model = Item
         fields = ('category', 'room_name', 'name', 'brand', 'model', 'serial_number', 'purchase_date', 'purchase_price', 'warranty', 'notes',)
  