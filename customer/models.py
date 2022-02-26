"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.db import models
from django.contrib.auth.models import User
from service.models import Service


class Booking(models.Model):
    """Model for customer booking"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.ForeignKey(
        Service, on_delete=models.CASCADE, limit_choices_to={'status': '1'})
    booking_date = models.DateField(unique=True)

    class Meta:
        """Class for ordering"""
        ordering = ['booking_date']

    def __str__(self):
        return str(self.user)
