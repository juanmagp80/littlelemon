from django.db import models

# Create your models here.
class menu(models.Model):
    ID = models.IntegerField( primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
class booking(models.Model):
    ID = models.IntegerField( primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    