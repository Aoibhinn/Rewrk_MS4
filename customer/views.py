"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.views import generic
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Booking
from .forms import CreateBookingForm


class BookingView(generic.ListView):
    """Booking list view"""
    model = Booking
    template_name = 'booked_services.html'

    def get_queryset(self):
        user = self.request.user
        booking_list = Booking.objects.filter(user=user)
        return booking_list


class CreateBookingView(SuccessMessageMixin, CreateView):
    """Create new booking view"""
    model = Booking
    form_class = CreateBookingForm
    template_name = 'create_booking.html'
    success_url = reverse_lazy('booked_services')
    success_message = 'Thank you for booking with us,\
                        a member of our team will reach out to you shortly!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBookingView, self).form_valid(form)
