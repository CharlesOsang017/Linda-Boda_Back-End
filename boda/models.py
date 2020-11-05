from django.db import models
import datetime as dt
from django_countries.fields import CountryField

# Create your models here

class Passenger(models.Model):
    name = models.CharField(max_length=40)
    city_destination = models.CharField(max_length=60)
    county = models.CharField(max_length=35)
    phone_number = models.DecimalField(decimal_places=2, max_digits=20)
    country = CountryField(blank_label='(select country)', default='KE')


    class Meta:
        verbose_name = 'Passenger'
        verbose_name_plural = 'Passengers'

