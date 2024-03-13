from django.db import models


class contactdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=1000, null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True, blank=True)
    message = models.CharField(max_length=2000, null=True, blank=True)


# Create your models here.

class Registerdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=1000, null=True, blank=True)
    Password = models.CharField(max_length=1000, null=True, blank=True)
    confirm_password = models.CharField(max_length=300, null=True, blank=True)
    Profile = models.ImageField(upload_to='profile_images', null=True, blank=True)


class CartDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Pro_Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)

class checkoutdb(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)
    city=models.CharField(max_length=100, null=True, blank=True)
    country=models.CharField(max_length=100, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

from django.db import models

# Create your models here.
