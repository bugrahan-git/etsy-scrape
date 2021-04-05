from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.URLField(max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name