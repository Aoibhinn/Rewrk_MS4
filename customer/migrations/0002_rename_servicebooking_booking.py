# Generated by Django 3.2.9 on 2021-11-29 20:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_alter_service_id'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceBooking',
            new_name='Booking',
        ),
    ]
