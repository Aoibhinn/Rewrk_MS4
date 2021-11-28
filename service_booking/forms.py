from django import forms
from service.models import Service



class BookingForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    telephone = forms.IntegerField(required=True)
    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(status=1), initial=0)
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))                   
