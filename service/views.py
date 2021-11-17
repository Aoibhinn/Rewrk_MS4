from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Service


class ServiceList(generic.ListView):
    model = Service
    context_object_name = 'services'
    queryset = Service.objects.filter(status=1).order_by('-created_on')
    template_name = 'services.html'



class ServiceDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Service.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
         
        return render(
            request,
            'service.html',
            {
                'service': Service
            }
        )
