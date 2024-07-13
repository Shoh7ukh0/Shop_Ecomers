from django.contrib import admin
from .models import Country, City, Profile

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['country']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'f_name', 'l_name', 'email', 'phone_number', 'country', 'city', 'address', 'post_code', 'photo']
    raw_id_fields = ['user']