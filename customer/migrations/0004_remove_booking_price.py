# Generated by Django 3.2 on 2022-02-26 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_booking_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='price',
        ),
    ]