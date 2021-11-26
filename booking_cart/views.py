from django.shortcuts import render

def view_bookings(request):
    """Renders the shopping bag page, will also handle all shopping bag processes"""

    return render(request, 'booking_cart/booking.html')
