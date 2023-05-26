from rest_framework import serializers
from .models import Client, Employee, OrderForm, OrderFormLine, Product


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'code']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'email', 'name']


class OrderFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderForm
        fields = ['id', 'number', 'client', 'date', 'status']


class OrderFormLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFormLine
        fields = ['id', 'order_form', 'product', 'quantity']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']
