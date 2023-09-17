from django.db import models
from django.utils.timezone import now
from django.core import serializers
import datetime
import uuid
import json

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    BIKE = "Bike"
    OTHER = "Other"
    CAR_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
        (BIKE, "Bike"),
        (OTHER, "Other")
    ]

    YEAR_CHOICES = []
    for r in range(1969, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    id = models.IntegerField(default=1, primary_key=True)
    model_type = models.CharField(null=False, max_length=15, choices=CAR_CHOICES, default=SEDAN)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return self.name + ", " + str(self.year) + ", " + self.model_type

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
