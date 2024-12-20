from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('seller', 'Seller'),
        ('delivery_person', 'Delivery Person'),
        ('delivery_hub', 'Delivery Hub'),
        ('customer', 'Customer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)





class CustomerAccount(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('erkak', 'Erkak'), ('ayol', 'Ayol')), null=True, blank=True)


class SellerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller_profile')
    store_name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='seller-logos/')
    banner = models.ImageField(upload_to='seller-banners/')
    store_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name


class DeliveryPersonProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='delivery_person_profile')
    vehicle_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class DeliveryHub(models.Model):
    hub_name = models.CharField(max_length=255)
    hub_address = models.TextField()
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    manager = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, related_name='hub_manager')

    def __str__(self):
        return self.hub_name