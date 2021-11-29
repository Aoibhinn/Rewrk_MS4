from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.BookingView.as_view(), name='booked_services'),
]
