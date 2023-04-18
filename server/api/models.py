from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OrderForm(models.Model):
    number = models.IntegerField
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField

    def __str__(self):
        return f"{self.number} {self.client.name}"


class OrderFormLine(models.Model):
    order_form = models.ForeignKey(OrderForm, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField

    def __str__(self):
        return f"{self.order_form.number} {self.product} {self.quantity}"


class Employee(models.Model):
    email = models.EmailField

    def __str__(self):
        return self.email
