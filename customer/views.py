from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Booking
from django.views import generic


class BookingView(generic.ListView):
    """Booking list view"""
    model = Booking
    template_name = 'booked_services.html'

    def get_queryset(self):
        user = self.request.user
        booking_list = Booking.objects.filter(user=user)
        return booking_list
