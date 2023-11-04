from django.db import models

# Create your models here.      
 
class Menu(models.Model):
       ID = models.IntegerField(primary_key=True)
       Title = models.CharField(max_length=255)
       Price = models.FloatField()
       Inventory = models.IntegerField()

class Booking(models.Model):
       ID = models.IntegerField(primary_key=True)
       Name = models.CharField(max_length=255)
       No_of_guests = models.IntegerField()
       BokkingDate = models.DateField()