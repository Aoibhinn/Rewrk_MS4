"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Booking Fields for display and filter"""
    list_display = ('user', 'booking_date', 'service_name')
    search_fields = ['booking_date', 'user', 'service_name']
    list_filter = ('booking_date', 'user')
