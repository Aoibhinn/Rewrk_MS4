"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django import forms
from django.contrib.auth.models import User
from service.models import Service
from .models import Booking


class CreateBookingForm(forms.ModelForm):
    """Create new booking form"""
    booking_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date', 'class': 'form-control'}))
    service_name = forms.ModelChoiceField(
        queryset=Service.objects.filter(status=1),
        empty_label="(Please select a service)",
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        """Meta class"""
        model = User
        model = Booking
        fields = (
            'booking_date',
            'service_name',
            )
