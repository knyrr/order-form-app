from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class OrderForm(models.Model):
    number = models.PositiveIntegerField(
        unique=True, validators=[MaxValueValidator(9999999999)])
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()

    class orderStatus(models.TextChoices):

        PENDING = "PENDING", _("Pending")
        DELIVERED = "DELIVERED", _("Delivered")

    status = models.CharField(
        max_length=255,
        choices=orderStatus.choices,
        default=orderStatus.PENDING)

    def __str__(self):
        return f"{self.number} {self.client.name} {self.date}"


class OrderFormLine(models.Model):
    order_form = models.ForeignKey(OrderForm, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=18, decimal_places=3)

    def __str__(self):
        return f"{self.order_form.number} {self.product} {self.quantity}"


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name} {self.email}"
