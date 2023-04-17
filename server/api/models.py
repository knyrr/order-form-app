from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
