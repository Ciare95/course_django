from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    date_create = models.DateTimeField(auto_now_add=True)
    update_create = models.DateTimeField(auto_now=True)
