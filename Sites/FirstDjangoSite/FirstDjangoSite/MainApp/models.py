from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} ({self.country})'


class Shop(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=1000, blank=True, null=True)
    site_url = models.CharField(max_length=100, blank=True)
    cities = models.ManyToManyField(City)

    def __str__(self):
        return f'{self.name} ({self.site_url})'


class Review(models.Model):
    name = models.CharField(max_length=60)
    text = models.TextField(max_length=2000, blank=True)
    rate = models.IntegerField(default=5)
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.rate}/10) ({self.shop})'
