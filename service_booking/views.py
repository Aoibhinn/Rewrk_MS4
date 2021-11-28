from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm

# Create your views here.


def booking(request):
    if request.method == 'GET':
        form = BookingForm()
    else:
        form = BookingForm(request.POST)
        if form.is_valid():
            subject = "Booking Request"
            body = {
                'message': form.cleaned_data['additional_information'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'telephone': form.cleaned_data['telephone'],
                'date': form.cleaned_data['date'],
                'service': form.cleaned_data['service'],
            }
            message = '\n'.join(map(str, body.values()))
            messages.success(request, 'Message sent successfully!')
            try:
                send_mail(subject, message, 'hello@rewrk.com', [
                    'hello@rewrk.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = BookingForm()
    return render(request, "booking.html", {'form': form})

