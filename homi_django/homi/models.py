from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.CharField(max_length=100)
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    purchase_date = models.CharField(max_length=100) 
    purchase_price = models.CharField(max_length=100) 
    warranty = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name

