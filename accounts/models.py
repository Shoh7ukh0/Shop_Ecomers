from django.db import models
from django.conf import settings

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    class Status(models.TextChoices):
        UZ = '+998', 'Uz'
        RU = '+7', 'Ru'
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number_code = models.CharField(choices=Status.choices, max_length=5, default=Status.UZ, null=True, blank=True)
    phone_number = models.CharField(max_length=9, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=250)
    post_code = models.CharField(max_length=7, null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'