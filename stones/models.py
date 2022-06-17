from django.db import models

# Create your models here.


class Stone(models.Model) :
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)     # we have define the decimal places
    inventory = models.IntegerField()