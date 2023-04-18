from django.contrib import admin
from .models import Client, Employee, OrderForm, OrderFormLine, Product

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(OrderForm)
admin.site.register(OrderFormLine)
admin.site.register(Product)
