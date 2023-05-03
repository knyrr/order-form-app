from .models import Client, Employee, OrderForm, OrderFormLine, Product
from .serializers import (
    ClientSerializer,
    EmployeeSerializer,
    OrderFormSerializer,
    OrderFormLineSerializer,
    ProductSerializer)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# region clients


@api_view(['GET', 'POST'])
def get_clients(request, format=None):

    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ClientSerializer(data=request. data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_client_by_id(request, id, format=None):
    try:
        client = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion

# region employees


@api_view(['GET', 'POST'])
def get_employees(request, format=None):

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request. data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_employee_by_id(request, id, format=None):
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion

# region products


@api_view(['GET', 'POST'])
def get_products(request, format=None):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request. data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_product_by_id(request, id, format=None):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion

# region order forms


@api_view(['GET', 'POST'])
def get_order_forms(request, format=None):

    if request.method == 'GET':
        orderForms = OrderForm.objects.all()
        serializer = OrderFormSerializer(orderForms, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderFormSerializer(data=request. data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_order_form_by_id(request, id, format=None):
    try:
        orderForm = OrderForm.objects.get(pk=id)
    except OrderForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderFormSerializer(orderForm)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderFormSerializer(orderForm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orderForm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion

# region order form lines


@api_view(['GET', 'POST'])
def get_order_form_lines(request, format=None):

    if request.method == 'GET':
        orderFormLines = OrderFormLine.objects.all()
        serializer = OrderFormLineSerializer(orderFormLines, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderFormLineSerializer(data=request. data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_order_form_line_by_id(request, id, format=None):
    try:
        orderFormLine = OrderFormLine.objects.get(pk=id)
    except OrderFormLine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderFormLineSerializer(orderFormLine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderFormLineSerializer(orderFormLine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        orderFormLine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# endregion
