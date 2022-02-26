from django.shortcuts import render
from .models import Booking
from django.views import generic
from django.views.generic import CreateView


class BookingView(generic.ListView):
    """Booking list view"""
    model = Booking
    template_name = 'booked_services.html'

    def get_queryset(self):
        user = self.request.user
        booking_list = Booking.objects.filter(user=user)
        return booking_list


