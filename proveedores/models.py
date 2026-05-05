from django.db import models

class Proveedor(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField()
    nit = models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return self.name
