from django.db import models
from django.utils.timezone import now

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# <HINT> Create a Car Model 

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    car_type = models.CharField(max_length=10, choices=CAR_TYPES)
    
    year = models.DateField()
    
    # Add other fields as needed

    def __str__(self):
        return f"{self.year} {self.make.name} {self.name}"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
