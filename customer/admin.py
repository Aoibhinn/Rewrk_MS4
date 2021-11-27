from django.contrib import admin
from .models import ServiceBooking


@admin.register(ServiceBooking)
class ServiceBookingAdmin(admin.ModelAdmin):
    """Booking Fields for display and filter"""
    list_display = ('user', 'booking_date', 'service_name')
    search_fields = ['booking_date', 'user', 'service_name']
    list_filter = ('booking_date', 'user')
