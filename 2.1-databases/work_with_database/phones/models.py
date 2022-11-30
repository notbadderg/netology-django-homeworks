from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)
