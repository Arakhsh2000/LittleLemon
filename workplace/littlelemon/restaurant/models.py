from django.db import models

# Create your models here.      
 
class Menu(models.Model):
       ID = models.AutoField(primary_key=True)
       Title = models.CharField(max_length=255)
       Price = models.FloatField()
       Inventory = models.IntegerField()

       def __str__(self):
              return f'{self.Title} : {str(self.Price)}'

class Booking(models.Model):
       ID = models.AutoField(primary_key=True)
       Name = models.CharField(max_length=255)
       No_of_guests = models.IntegerField()
       BookingDate = models.DateField()