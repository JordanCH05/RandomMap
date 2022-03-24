from django.db import models


class Map(models.Model):
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    destination = models.IntegerField(default=1)
    distance = models.DecimalField(max_digits=5, decimal_places=4)
