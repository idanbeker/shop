from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    name = models.CharField(max_length=200)
    cart = models.CharField(max_length=200)
    cart_size = models.IntegerField()
    page_index = models.IntegerField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=400)
    pic_url = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

