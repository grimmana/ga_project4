# homi/forms.py
from django import forms
from .models import Room, Item

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name')