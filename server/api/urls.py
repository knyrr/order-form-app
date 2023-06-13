"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import send_pdf_email

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/clients/', views.get_clients),
    path('api/clients/<int:id>', views.get_client_by_id),

    path('api/employees/', views.get_employees),
    path('api/employees/<int:id>', views.get_employee_by_id),

    path('api/products/', views.get_products),
    path('api/products/<int:id>', views.get_product_by_id),

    path('api/order-forms/', views.get_order_forms),
    path('api/order-forms/<int:id>', views.get_order_form_by_id),

    path('api/order-form-lines/', views.get_order_form_lines),
    path('api/order-form-lines/<int:id>', views.get_order_form_line_by_id),

    path('api/send-pdf/', views.send_pdf_email, name='send_pdf_email'),



]

urlpatterns = format_suffix_patterns(urlpatterns)
