"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm


def booking(request):
    """Booking app view for submission of form"""
    if request.method == 'GET':
        form = BookingForm()
    else:
        form = BookingForm(request.POST)
        if form.is_valid():
            subject = "Booking Request"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'telephone': form.cleaned_data['telephone'],
                'service': form.cleaned_data['service'],
            }
            message = '\n'.join(map(str, body.values()))
            messages.success(request, 'Thank you for booking one of our Services.\
                             A member of our team will be in\
                                 touch with you shortly!')
            try:
                send_mail(subject, message, 'hello@rewrk.com', [
                    'hello@rewrk.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    form = BookingForm()
    return render(request, "booking.html", {'form': form})
