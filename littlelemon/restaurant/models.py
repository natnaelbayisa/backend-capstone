from django.db import models

# Create your models here.

# Booking model
class Booking(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

# create user
class NewUser(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   phoneNumber = models.CharField(max_length=200)
   password = models.CharField(max_length=500)

   def __str__(self) -> str:
          return self.first_name

# Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self) -> str:
      return f'{self.name} : {str(self.price)}' 
   
   # sorting items by their alphabet
   class Meta:
      ordering = ('name',) 