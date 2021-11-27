from django.shortcuts import render
from django.views.generic import TemplateView

class CustomerViewProfile(TemplateView):
    """Customer profile page view"""
    template_name = 'profile.html'

    def about(self, request):
        """Return render view for customer view profile page"""
        return render(request, 'profile.html')