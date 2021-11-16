from django.shortcuts import render
from django.views import generic
from .models import Service


class ServiceList(generic.ListView):
    model = Service
    context_object_name = 'services'
    queryset = Service.objects.filter(status=1).order_by('-created_on')
    template_name = 'services.html'

 
