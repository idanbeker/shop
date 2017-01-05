from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    cart = models.CharField(max_length=200)


class Item(models.Model):
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
