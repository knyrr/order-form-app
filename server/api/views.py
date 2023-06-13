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
from django.http import HttpResponse
# from django.core.mail import EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

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

# region send pdf

# Setup port number and server name


def send_pdf_email(request):
    smtp_port = 587                 # Standard secure SMTP port
    smtp_server = "smtp.gmail.com"  # Google SMTP Server

    # Set up the email lists
    email_from = os.environ.get('EMAIL_HOST_USER')
    pswd = os.environ.get('EMAIL_HOST_PASSWORD')

    email_to = "rynk@tlu.ee"

    subject = "New email from TIE with attachments!!"

    body = f"""
        line 1
        line 2
        line 3
        etc
        """

    # make a MIME object to define parts of the email
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    # Attach the body of the message
    msg.attach(MIMEText(body, 'plain'))

    # Define the file to attach
    filename = "./random_data.csv"

    # Open the file in python as a binary
    attachment = open(filename, 'rb')  # r for read and b for binary

    # Encode as base 64
    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header(
        'Content-Disposition', "attachment; filename= " + filename)
    msg.attach(attachment_package)

    # Cast as string
    text = msg.as_string()

    # Connect with the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Succesfully connected to server")
    print()

    # Send emails to "person" as list is iterated
    print(f"Sending email to: {person}...")
    TIE_server.sendmail(email_from, person, text)
    print(f"Email sent to: {person}")
    print()

    # Close the port
    TIE_server.quit()

    return HttpResponse('Email sent with PDF attachment.')


# @api_view(['GET', 'PUT', 'DELETE'])


# def send_pdf_email(request):
#     # Generate the PDF
#     # generate_pdf()

#     # Create an email message object
#     email = EmailMessage(
#         'PDF Attachment',
#         'Please find attached the PDF file.',
#         'martin.rynk@gmail.com',  # Replace with sender's email address
#         ['martin.runk@tlu.ee'],  # Replace with recipient's email address(es)
#         # cc=['cc@example.com'],  # Replace with CC email address(es) if needed
#     )

#     # Attach the PDF file to the email
#     # email.attach_file('path/to/your/pdf.pdf')

#     # Send the email
#     email.send()

#     # send_mail('Test', 'This is a test', 'martin.rynk@gmail.com',
#     #           ['rynk@tlu.ee'], fail_silently=False)

#     return HttpResponse('Email sent with PDF attachment.')


# endregion
