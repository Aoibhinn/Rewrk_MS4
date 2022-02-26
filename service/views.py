"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from django.views import generic
from django.views.generic import DetailView
from .models import Service


class ServiceList(generic.ListView):
    """
    Services List View
    """
    model = Service
    context_object_name = 'services'
    queryset = Service.objects.filter(status=1).order_by('-created_on')
    template_name = 'services.html'


class ServiceDetail(DetailView):
    """
    Services Detail View
    """
    model = Service
    template_name = 'service.html'
    queryset = Service.objects.filter(status=1)
