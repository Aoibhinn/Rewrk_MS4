from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Service
from django.views.generic import DetailView


class ServiceList(generic.ListView):
    model = Service
    context_object_name = 'services'
    queryset = Service.objects.filter(status=1).order_by('-created_on')
    template_name = 'services.html'



class ServiceDetail(DetailView):
    model = Service
    template_name = 'service.html'
    queryset = Service.objects.filter(status=1)