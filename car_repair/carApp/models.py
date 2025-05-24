from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    country = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    type = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    maxSpeed = models.IntegerField()
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class WorkShop(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    oldCarRepair = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Repair(models.Model):
    code = models.CharField(max_length=15)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='data', blank=True)
    carDetails = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class WorkShopManufacturer(models.Model):
    workShop = models.ForeignKey(WorkShop, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)



class FixRequest(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    car_model = models.CharField(max_length=100)
    issue_description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.car_model}"