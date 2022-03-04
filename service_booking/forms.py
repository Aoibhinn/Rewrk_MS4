"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django import forms
from service.models import Service


class BookingForm(forms.Form):
    """Booking form to register for a course"""
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    telephone = forms.IntegerField(required=True)
    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(status=1), initial=0)
    further_information_about_your_business = forms.CharField(
        widget=forms.Textarea, required=False)
