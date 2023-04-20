# Generated by Django 4.2 on 2023-04-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_employee_email_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderform',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='orderform',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orderformline',
            name='quantity',
            field=models.DecimalField(decimal_places=3, max_digits=18, null=True),
        ),
    ]