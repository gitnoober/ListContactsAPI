from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Creating a Contact model

class Contact(models.Model): #this is basically what a contact will look like
    owner = models.ForeignKey(to=User , on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_fav = models.BooleanField(default=False) #by default you have no favs
    

    