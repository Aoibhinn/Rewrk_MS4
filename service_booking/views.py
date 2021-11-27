from django.shortcuts import render

# Create your views here.


def servicebooking(request):
    template = 'service_booking/booking.html'
    return render(request, template)