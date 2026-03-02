from django.db import models


class Client(models.Model):

    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    nit = models.PositiveBigIntegerField(default=0, unique=True, null=False)
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.name
