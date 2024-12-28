from django.db import models

# Create your models here.
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Brand Name")
    country = models.CharField(max_length=255, verbose_name="Country of Origin")

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255, verbose_name="Car Model")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    description = models.TextField(verbose_name="Car Description")

    def __str__(self):
        return self.model
