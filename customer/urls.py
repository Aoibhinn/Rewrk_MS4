"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.urls import path
from . import views
from .views import CreateBookingView, EditBooking, DeleteBooking

urlpatterns = [
    path('customer/', views.BookingView.as_view(), name='booked_services'),
    path('create_booking/',
         CreateBookingView.as_view(),
         name="create_booking"),
    path('booked_services/<int:pk>/delete',
         DeleteBooking.as_view(), name="delete_booking"),
    path(
        'booked_services/edit/<int:pk>',
        EditBooking.as_view(), name="edit_booking"),
]
