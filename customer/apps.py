"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.apps import AppConfig


class CustomerConfig(AppConfig):
    """
    Customer app.py
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
